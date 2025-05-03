from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login, logout
from .models import User,Taskmanagement

# Create your views here.


class UserManagement:

    def UserManagement(request):
        if request.method == 'GET':
            return render(request,'login/login.html')
        elif request.method == 'POST':
            if "username" in request.POST and "password" in request.POST:
                username = request.POST.get('username')
                password = request.POST.get('password')
                print(username,password)
                user = authenticate(request,username=username,password=password)
                print("hello user",user)
                if user is not None:
                    login(request,user)
                    print("user print : ",user.is_manager)
                    if user.is_superuser:
                        return redirect('superadminlist')
                    elif user.is_manager or user.is_marketingmanage or user.is_user:
                        return redirect('taskmanagement')
                else:
                    return HttpResponse('failed')
            else:
                return HttpResponse('failed')
    
    def SuperAdmin(request):
        context = {}
        if request.method == 'GET':
            context['users'] = User.objects.all()
            return render(request,'superadmin/usertablelist.html',context)
        elif request.method == 'POST':
            user_role = ["is_manager","is_marketingmanage","is_user","is_superuser","is_staff"]
            userdb = User.objects.create_user(
                username = request.POST.get('username'),
                email = request.POST.get('username'),
                password = request.POST.get('password'),
            )
            userdb.save()
            user_db = User.objects.get(id=userdb.id)
            for role in user_role:
                setattr(user_db,role,False)
            setattr(user_db,request.POST.get('usertype'),True)
            user_db.save()
            return redirect('superadminlist')
    
    def logout_view(request):
        logout(request)
        return redirect('UserManagement')


class TaskManagement:

    def TaskManagement(request):
        if request.method == 'GET':
            context = {}
            context['users'] = User.objects.filter(is_user=True)
            context['tasks'] = Taskmanagement.objects.all()
            print(context['tasks'])
            for task in context['tasks']:
                print(task.title)
            return render(request,'task/taskmanagemenlist.html',context)
        elif request.method == 'POST':
            print("method is post")
            Taskmanagement.objects.create(
                title = request.POST.get('tasktile'),
                user = User.objects.get(username=request.POST.get('username')),
                date = request.POST.get('datetask'),
            )
            return redirect('taskmanagement')
        
    def EditTask(request,id):
        context = {}
        if request.method == 'GET':
            context['task'] = Taskmanagement.objects.get(id=id)
            context['users'] = User.objects.filter(is_user=True)
            return render(request, 'task/editTask.html',context)
        elif request.method == 'POST':
            Taskmanagement.objects.filter(id=id).update(
                title = request.POST.get('tittle'),
                user = User.objects.get(username=request.POST.get('username')),
                date = request.POST.get('dateassign'),
            )
            return redirect('taskmanagement')
    
    def DeleteTask(request,id):
        if request.method == 'POST':
            Taskmanagement.objects.get(id=id).delete()
            return redirect('taskmanagement')