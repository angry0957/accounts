from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Lawyer
from django.contrib.auth import authenticate, login
import datetime
import json
# Create your views here.

def signup(request):
	Email = request.POST['Email'] 
	Password = request.POST['Password'] 
	BusinessAddress = request.POST['BusinessAddress'] 
	City = request.POST['City'] 
	State = request.POST['State'] 
	PhoneNumber = request.POST.get('PhoneNumber', False) 
	LicenseIDNumber = request.POST.get('LicenseIDNumber', False)
	YearAdmitted = request.POST.get('YearAdmitted', datetime.datetime.now())
	HCRNo = request.POST.get('hcr_number')

	obj  =  Lawyer(username=Email,email=Email,password=Password,state=State,city=City,buisness_address=BusinessAddress,phone_number=PhoneNumber,liscence_number=LicenseIDNumber,year_admitted=YearAdmitted,hcr_number=HCRNo)
	obj.save()
	login(request,obj)
	return JsonResponse({"HAHA":"SUCCESS"})


def lawyers(request):
	return render(request, "index.html", {})

def login1(request):
	Email = request.POST['Email'] 
	Password = request.POST['Password'] 
	obj  =  authenticate(username=Email,password=Password)
	if obj is not None:
		login(request,obj)
		return JsonResponse({"HAHA":"SUCCESS"})

	data = {
		"data":"FAILED",
		"Email": Email,
		"password": Password,
		"obj": obj
	}
	return JsonResponse(data)

def read(request):
	data = Lawyer.objects.all()
	return JsonResponse({"data":data[0].username})

def delete(request):
	data = Lawyer.objects.filter(username="user6@gmail.com")
	return JsonResponse({"data":data.delete()})

def update(request):
	data = Lawyer.objects.filter(username="user5@gmail.com")
	return JsonResponse({"data":data.update(phone_number="0321-4445-100")})
