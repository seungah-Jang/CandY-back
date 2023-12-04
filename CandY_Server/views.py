from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from .serializers import RegisterSerializer

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
@csrf_exempt
def LoginView(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        user = authenticate(request, user_id=user_id, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Login failed'}, status=401)

    return JsonResponse({'message': 'Invalid method'}, status=400)


# Create your views here.
#Resgister (Sign Up)
#class RegisterView(generics.CreateAPIView):
#    serializer_class = RegisterSerializer
'''
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            user_id = request.data.get('user_id')
            password = request.data.get('password')

            user = authenticate(request, user_id = user_id, password = password)

            if user is not None:
                login(request,user)
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return JsonResponse({'access_token':access_token, 'message':'Login Successful'})
            else:
                return JsonResponse({'message':'Login failed'},status=status.HTTP_401_UNAUTHORIZED)
        return JsonResponse({'message':'Invalid method'},status=400)   
'''

        
