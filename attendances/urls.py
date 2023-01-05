from django.urls import path
from . import views

app_name = 'attendances'

urlpatterns = [
    path('', views.AttendancesList.as_view()),
    path('<int:pk>/', views.AttendancesDetail.as_view()),
]