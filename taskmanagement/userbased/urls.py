from django.urls import path
from .views import UserManagement,TaskManagement

superadminurlpatterns = [
    path('', UserManagement.UserManagement, name='UserManagement'),
    path('SuperAdmin', UserManagement.SuperAdmin, name='superadminlist'),
    path('logout/', UserManagement.logout_view, name='logout'),
]

TaskManagementurlpatterns = [
    path('TaskManagement/', TaskManagement.TaskManagement, name='taskmanagement'),
    path('EditTask/<int:id>', TaskManagement.EditTask, name='edittask'),
    path('DeleteTask/<int:id>', TaskManagement.DeleteTask, name='deletetask'),
]

urlpatterns = superadminurlpatterns+TaskManagementurlpatterns