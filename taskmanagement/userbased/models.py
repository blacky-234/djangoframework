from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

def get_current_date():
    return datetime.date.today()

class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_marketingmanage = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class Taskmanagement(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    current_date = models.DateField(default=get_current_date)