from django.shortcuts import render

# Create your views here.

class SystemStatus:
    def system_status(request):
        if request.method == 'GET':
            return render(request, 'systemstatus.html')
