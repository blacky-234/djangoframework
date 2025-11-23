from django.shortcuts import render

# Create your views here.


class Auth:


    def Root_Views(request):
        print("request captured")

        return render(request, 'rootpage/index.html')