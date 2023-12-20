from django.shortcuts import render

from django.http import JsonResponse
from django.db import connection

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.views import View

import json

from datetime import datetime, timedelta
# GET

##1 If you click the date in calendar, you can get the concentration average score for the day.  
def Day_Concentration_Avg(request, date): # date is required by client
    if request.method == 'GET':
        query = """
            SELECT AVG(concentration_score_avg) AS day_concentration_avg
            FROM TB_SESSION_RESULT
            WHERE DATE(session_start_time) = %s
        """    
        with connection.cursor() as cursor:
            cursor.execute(query, [date])   
            row = cursor.fetchone()

        day_concentration_avg = row[0] if row else None

        if day_concentration_avg is not None:
            return JsonResponse({
                'result' : True,
                'day_concentration_avg': day_concentration_avg,
                'message' : 'Data Exites'
                })
        else:
            return JsonResponse({
                'result' :  False,
                'day_concentration_avg' : None,
                'message':'No data available for day',
                })
    else:
        return JsonResponse({
            'result' : False,
            'day_concentration_avg' : None,
            'message':'Method Not Allowed'
            },status=405)


##2 Home Screen : You are in the Home Screen, you can get the concentration average score for today
def Today_Concentration_Avg(request):
    if request.method == 'GET':

        # today's date
        today = datetime.now().date()

        # yesterday date
        #yesterday = today - timedelta(days=1)

        query = """
            SELECT AVG(concentration_score_avg) AS today_concentration_avg
            FROM TB_SESSION_RESULT
            WHERE DATE(session_start_time) = %s
        """    
        with connection.cursor() as cursor:
            cursor.execute(query, [today])   
            row = cursor.fetchone()

        today_concentration_avg = row[0] if row else None
        if today_concentration_avg is not None:
            return JsonResponse({
                'result' : True,
                'today_concentration_avg': today_concentration_avg,
                'message' : 'Data Exites'
                })
        else:
            return JsonResponse({
                'result' :  False,
                'today_concentration_avg' : 0,
                'message':'No data available for today'
                })

    else:
        return JsonResponse({
            'result' : False,
            'today_concentration_avg' : None,
            'message':'Method Not Allowed'
            },status = 405)

##3 Show the UserID at the top (HoT)
def Show_UserID(request) : 
    if request.method =='GET':
        query = """
            SELECT user_id from TB_MEMBER
            WHERE user_id = "HoT"
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()

        user_id = row[0] if row else None
        return JsonResponse({'result': True, 'user_id':user_id, 'message':'We are the Team HoT!'})
    else:
        return JsonResponse({'result':False, 'user_id':None, 'message':'Method Not Allowed'}, status=405)


##4 Daily_Report : Send the data about Day_Concentration_Avg and Daily_Report(session_id, session_place, session_start_time)
def Daily_Report(request,UserId,date):
    if request.method == 'GET':
    
        query = """
            SELECT AVG(concentration_score_avg) AS day_concentration_avg
            FROM TB_SESSION_RESULT
            WHERE DATE(session_start_time) = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(query,[date])
            row = cursor.fetchone()    
            
        day_concentration_avg = row[0]

            
        query = """
            SELECT session_id, session_place, TIME(session_start_time) AS session_start_time
            FROM TB_SESSION_RESULT
            WHERE user_id=%s AND DATE(session_start_time) = %s 
        """
        with connection.cursor() as cursor:
            cursor.execute(query,[UserId,date])
            rows = cursor.fetchall()
                
                
            Daily_Report_All = []
            for row in rows:
                Daily_Report = {
                    'session_id' :row[0],
                    'session_place' :row[1],
                    'session_start_time' : row[2].strftime('%H:%M:%S')
                }
                Daily_Report_All.append(Daily_Report)
        if len(Daily_Report_All) != 0 :
            return JsonResponse({'result':True,'day_concentration_avg':day_concentration_avg,'Daily_Report_All':Daily_Report_All,'message':'Success'})
        else:
            return JsonResponse({'result':False,'day_concentration_avg':0,'Daily_Report_All':None,'message':'Data not existed'})

            
    else:
        return JsonResponse({'result':False, 'day_concentration_avg':None, 'Daily_Report_All':None,'message':'Method Not Allowed'}, status=405)


##5 Session Report : Send the information on measured features 
def Session_Report (request, UserId, SessionId):
    if request.method == 'GET':
        query = """
            SELECT 
                AVG(hr) AS hr_avg,
                AVG(hrv) AS hrv_avg,
                AVG(body_movement) AS body_movement_avg,
                AVG(deep_sleep_minutes) AS deep_sleep_minutes_avg,
                AVG(eda) AS eda_avg,
                AVG(wrist_temperature) AS wrist_temperature_avg,
                AVG(concentration_score) AS session_concentration_avg
            FROM TB_FITBIT
            WHERE user_id = %s AND session_id = %s
        """
        with connection.cursor() as cursor:
            cursor.execute(query,[UserId, SessionId])
            row = cursor.fetchone()

        if row is not None:
            Session_Data_Avg = {
                "hr" : row[0],
                "hrv" : row[1],
                "body_movement" : row[2],
                "deep_sleep_minutes" : row[3],
                "eda" : row[4],
                "wrist_temperature" :row[5],
                "session_concentration_avg" : row[6]
            }

        if Session_Data_Avg is not None:
            return JsonResponse({
                'result' : True,
                'Session_Data_Avg' : Session_Data_Avg,
                'message' : 'Data Exist'
                })
        else:
            return JsonResponse({
                'result' :  False,
                'Session_Data_Avg' : None,
                'message':'No data'
                })
    else:
        return JsonResponse({
            'result' : False,
            'Session_Data_Avg' : None,
            'message':'Method Not Allowed'
            }, status = 405)


##6 Send the session dates for the user for marking on the calendar
def User_Session_All (request,UserId):
    if request.method == 'GET':
    
        query = """
            SELECT DISTINCT DATE(session_start_time) AS User_Session_All
            FROM TB_SESSION_RESULT
            WHERE user_id = % s
        """

        with connection.cursor() as cursor:
            cursor.execute(query,[UserId])
            rows = cursor.fetchall()
            User_Session_All = [str(row[0]) for row in rows]

            #Monthly_Session_Date = json.dumps(date_list, ensure_ascii=False)

            
        if len(User_Session_All) != 0 :
            return JsonResponse({'result':True,'User_Session_All':User_Session_All,'message':'Success'})
        else:
            return JsonResponse({'result':False,'User_Session_All':None,'message':'Data not existed'})

            
    else:
        return JsonResponse({'result':False, 'User_Session_All':None,'message':'Method Not Allowed'}, status=405)


#POST

interval_minutes = 5
##1 If the client clicks the finish button, session information is inserted into the TB_SESSION_RESULT
## Bio data is loaded into the TB_FITBIT
@csrf_exempt    
def Create_Session_Result (request) :
    if request.method == 'POST':
        try:
            #POST Data
            data = json.loads(request.body.decode('utf-8'))
            user_id = data.get('user_id', None)
            session_place = data.get('session_place',None)
            session_start_time = data.get('session_start_time',None)
            session_end_time = data.get('session_end_time',None)

            with connection.cursor() as cursor:
                
                #Session result is inserted into the TB_SESSION_RESULT
                query = """
                    INSERT INTO TB_SESSION_RESULT (user_id, session_place, session_start_time, session_end_time)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, [user_id, session_place, session_start_time, session_end_time])

                # Get the last inserted session_id
                session_id = cursor.lastrowid

                # Bio data is loaded into the TB_FITBIT

                ## (1) Caculate the number of data to load    
                session_end_time = datetime.strptime(session_end_time, "%Y-%m-%d %H:%M:%S")
                session_start_time = datetime.strptime(session_start_time, "%Y-%m-%d %H:%M:%S")
                
                total_duration = (session_end_time - session_start_time).total_seconds() / 60
                intervals_cnt = int( total_duration / interval_minutes ) + 1
                current_time = session_start_time

                ## (2) Get the data from TB_DATA and load it into TB_FITBIT
                query = """
                    SELECT hr,hrv, body_movement, deep_sleep_minutes, eda, wrist_temperature, concentration_score
                    FROM TB_DATA
                    LIMIT %s
                """
                cursor.execute(query, [intervals_cnt])
                rows = cursor.fetchall()

                for row in rows:
                    query = """
                        INSERT INTO TB_FITBIT (user_id, session_id, datetime, hr, hrv, body_movement, deep_sleep_minutes, eda, wrist_temperature, concentration_score)
                        VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(query,[user_id, session_id, current_time, *row])
                    current_time = current_time + timedelta(minutes = interval_minutes)
                
                  
                # Caculate session_concentration_avg from TB_FITBIT
                query ="""
                    SELECT AVG(concentration_score) AS session_concentration_avg
                    FROM TB_FITBIT
                    WHERE user_id = %s AND session_id = %s
                """
                cursor.execute(query, [user_id, session_id])
                row = cursor.fetchone()
                session_concentration_avg = row[0]

                # Update TB_SESSION_RESULT about session_concentration_avg
                query = """
                    UPDATE TB_SESSION_RESULT
                    SET concentration_score_avg = %s
                    WHERE session_id = %s
                """
                cursor.execute(query, [session_concentration_avg,session_id])

                return JsonResponse({'result':True, 'session_id':session_id, 'message':'Success'},status=200)
        except Exception as e:
            return JsonResponse({'result': False, 'session_id':None, 'message':str(e)},status=500)    
            




            
