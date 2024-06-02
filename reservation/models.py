from django.db import models

# Create your models here.
class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    end_time = models.TimeField()
    name = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    floor = models.IntegerField()
    day = models.IntegerField()
    start_time = models.TimeField()
    room = models.IntegerField()