from django.urls import path
from .views import SystemStatus,ReportStatus

app_name = 'websocket'

SystemPath = [
    path('',SystemStatus.system_status, name='systemstatus'),
]

Report = [
    path('start/', ReportStatus.start_report_job),
    path('progress/<str:job_id>/', ReportStatus.check_report_progress),
]


urlpatterns = SystemPath+Report