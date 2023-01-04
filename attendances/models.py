from django.db import models
from django.conf import settings
# Create your models here.

class Attendances(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attendaces')
    check_in = models.DateTimeField(null=True, auto_now_add=True)
    check_out = models.DateTimeField(null=True, blank=True)
    status = models.CharField(null=True, max_length=30)

class AttendancesCount(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='count')
    attendance_days = models.IntegerField(null=True)
    absent_days = models.IntegerField(null=True)
    tardy_days = models.IntegerField(null=True)
    leave_days = models.IntegerField(null=True)


class GroupInfo(models.Model):
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='group')
    name = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class BelongGroup(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='belong')
    group = models.ForeignKey(GroupInfo, on_delete=models.CASCADE, related_name='members')