"""
URL configuration for AttenBack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from attendance.views import *

from authentication.views import *

urlpatterns = [
    path('', attendance_home,name="attendance_home"),
    path('admin/', admin.site.urls),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/register/', RegistrationView.as_view(), name='register'),
    path('api/attendance/', AttendancePost.as_view(), name='attendance'),
    path('api/ApplyLeave/', ApplyLeave.as_view(), name='ApplyLeave'),
    path('api/ApplyCorrection/', ApplyCorrection.as_view(), name='ApplyCorrection'),
    path('api/ApplyEarlyLeave/', ApplyEarlyLeave.as_view(), name='ApplyEarlyLeave'),
    path('api/getUserDetails/', getUserDetails.as_view(), name='getUserDetails'),
    path('api/GetLeaveTypeList', GetLeaveTypeList, name='GetLeaveTypeList'),
    path('api/FetchRecentAttendance', FetchRecentAttendance, name='FetchRecentAttendance'),
    path('api/FetchRecentLeaves', FetchRecentLeaves, name='FetchRecentLeaves'),
    path('api/FetchCurrentAttendance', FetchCurrentAttendance, name='FetchCurrentAttendance'),
    path('api/Alerts', AlertsPost.as_view(), name='AlertsPost'),
    path('api/AttendanceCorrectionUpdate', AttendanceCorrectionUpdate.as_view(), name='AttendanceCorrectionUpdate'),
    path('api/LeaveStatusUpdate', LeaveStatusUpdate.as_view(), name='LeaveStatusUpdate'),
    path('api/ApplyLeaveESS', ApplyLeaveESS.as_view(), name='ApplyLeaveESS'),
    path('api/getAlertList', getAlertList, name='getAlertList'),
]
