from django.shortcuts import render
from django.http import JsonResponse
from .tasks import generate_report
from .models import ReportJob
import uuid
import asyncio

# Create your views here.

class SystemStatus:
    def system_status(request):
        if request.method == 'GET':
            return render(request, 'systemstatus.html')

class ReportStatus:
    # Normal endpoint starts celery task
    def start_report_job(request):
        job_id = str(uuid.uuid4())
        ReportJob.objects.create(job_id=job_id, status="started")
        generate_report.delay(job_id)
        return JsonResponse({"job_id": job_id, "message": "Report started"})

    # Async endpoint for checking progress (non-blocking)
    async def check_report_progress(request, job_id):
        await asyncio.sleep(0)  # allows event loop to switch task
        job = ReportJob.objects.get(job_id=job_id)
        return JsonResponse({"job_id": job_id, "progress": job.progress, "status": job.status})
