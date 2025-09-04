from django.shortcuts import render

# Create your views here.


class Auth:


    def Login_Views(request):
        print("request captured")

        return render(request, 'login.html')