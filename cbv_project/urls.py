"""
URL configuration for cbv_project project.

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
from app.views import *
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv_string/',fbv_string,name='fbv_string'),
    path('cbv_string/',cbv_string.as_view(),name='cbv_string'),
    path('fvb_temp/',fvb_temp,name='fvb_temp.html'),
    path('cbv_temp/',cbv_temp.as_view(),name='cbv_temp'),
    path('cbv_render/',Cbv_render.as_view(),name='cbv_render'),
    path('insert_fbv/',insert_fbv,name='insert_fbv'),
    path('cbv_insert/',Cbv_insert.as_view(),name='cbv_insert'),
    path('suffix/',TemplateView.as_view(template_name='new_temp.html'),name='suffix'),
    path('tempDataRender/',TempDataRender.as_view(),name='tempDataRender'),
    path('TVStudentForm/',TVStudentForm.as_view(),name='TVStudentForm'),
    path('FVform/',FVform.as_view(),name='FVform'),
]
