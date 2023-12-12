"""
URL configuration for myproject project.

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
from django.urls import path
from .views import Day_Concentration_Avg,Today_Concentration_Avg, Session_Report, Create_Session_Result,Show_UserID,Daily_Report, User_Session_All

urlpatterns = [
    path("admin/", admin.site.urls),
    path('Day_Avg/<str:date>/', Day_Concentration_Avg),
    path('Today_Avg/',Today_Concentration_Avg),
    path('Session_Report/<str:UserId>/<int:SessionId>/', Session_Report),
    path('Create_Session_Result/',Create_Session_Result),
    path('Show_UserID/',Show_UserID),
    path('Daily_Report/<str:UserId>/<str:date>/',Daily_Report),
    path('User_Session_All/<str:UserId>/',User_Session_All)
]
