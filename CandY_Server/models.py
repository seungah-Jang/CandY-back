from django.db import models

# Create your models here.

class TbFitbit(models.Model):
    idx = models.IntegerField(primary_key=True)
    session_id = models.CharField(max_length=150)
    user_id = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    hr = models.FloatField(blank=True, null=True)
    hrv = models.FloatField(blank=True, null=True)
    coherence = models.FloatField(blank=True, null=True)
    bm = models.IntegerField(blank=True, null=True)
    sleep = models.IntegerField(blank=True, null=True)
    eda = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    concentration_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_Fitbit'


class TbMember(models.Model):
    user_id = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=50)
    device_check = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_Member'


class TbSessionResult(models.Model):
    session_id = models.CharField(primary_key=True, max_length=150)
    user_id = models.CharField(max_length=30)
    input_place = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    concentration_score_avg = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_Session_Result'