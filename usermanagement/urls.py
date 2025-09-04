from django.urls import path
from .views import Auth

Auth = [
    path('', Auth.Login_Views, name='login'),
]



urlpatterns = Auth