import time
from celery import shared_task
from .models import ReportJob
import uuid


@shared_task(bind=True)
def generate_report(self, job_id):
    for i in range(1, 11):
        time.sleep(60)  # 10 steps × 1 min = 10 min
        percent = i * 10
        ReportJob.objects.filter(job_id=job_id).update(progress=percent)
        self.update_state(state="PROGRESS", meta={"progress": percent})
    
    # task ends normally → worker exits quietly
    ReportJob.objects.filter(job_id=job_id).update(status="completed")
    print("✅ Report completed. Celery worker exiting quietly...")
    return "Report ready"

