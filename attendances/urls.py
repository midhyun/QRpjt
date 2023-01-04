from django.urls import path
from . import views

app_name = 'attendances'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkin', views.check_in, name='check_in'),
]