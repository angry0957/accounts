"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include 
from django.views.generic.base import TemplateView
from Lawyer import views as myview
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
	path('loginClient/', myview.login1),
    path('read/', myview.read),
    path('delete/', myview.delete),
    path('update/', myview.update),


    path('adduser/', myview.signup),
    path('', RedirectView.as_view(pattern_name='SignupLawyer', permanent=False)),
    path('SignupLawyer/', myview.lawyers , name='SignupLawyer'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signin', TemplateView.as_view(template_name='SignIn.html'),name='login'),
    path('signup', TemplateView.as_view(template_name='SignUp.html'),name='signup'),
    path('home', TemplateView.as_view(template_name='index.html'),name='home'),

]
