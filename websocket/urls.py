from django.urls import path
from .views import SystemStatus

app_name = 'websocket'

SystemPath = [
    path('',SystemStatus.system_status, name='systemstatus'),
]



urlpatterns = SystemPath