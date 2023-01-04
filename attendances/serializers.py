from rest_framework import serializers
from .models import Attendances, AttendancesCount, GroupInfo, BelongGroup

class AttendancesSerializer(serializers.Serializer):
    class Meta:
        model = Attendances
        fields = ['users', 'check_in', 'check_out', 'status']

class AttendancesCountSerializer(serializers.Serializer):
    class Meta:
        model = AttendancesCount
        fields = ['users', 'attendance_days', 'absent_days', 'tardy_days', 'leave_days']

class GroupInfoSerializer(serializers.Serializer):
    class Meta:
        model = GroupInfo
        fields = ['host', 'name', 'content', 'created_at']

class BelongGroupSerializer(serializers.Serializer):
    class Meta:
        model = BelongGroup
        fields = ['users', 'group']