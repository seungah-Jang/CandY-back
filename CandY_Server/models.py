from django.db import models

# Create your models here.

class TB_FITBIT (models.Model):
    experiment_idx = models.IntegerField(primary_key=True)
    session_id = models.CharField(max_length=150)
    user_id = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    hr = models.FloatField(blank=True, null=True)
    hrv = models.FloatField(blank=True, null=True)
    coherence = models.FloatField(blank=True, null=True)
    body_movement = models.IntegerField(blank=True, null=True)
    deep_sleep_minutes = models.IntegerField(blank=True, null=True)
    eda = models.FloatField(blank=True, null=True)
    wrist_temperature = models.FloatField(blank=True, null=True)
    concentration_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_FITBIT'


class TB_MEMBER(models.Model):
    user_id = models.CharField(primary_key=True, max_length=30)
    user_pw = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'TB_MEMBER'


class TB_SESSION_RESULT(models.Model):
    session_id = models.CharField(primary_key=True, max_length=150)
    user_id = models.CharField(max_length=30)
    session_place = models.CharField(max_length=100, blank=True, null=True)
    session_start_time = models.DateTimeField()
    session_end_time = models.DateTimeField()
    concentration_score_avg = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_SESSION_RESULT'