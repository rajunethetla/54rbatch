from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import Student

# Create your views here.
def sample(request):
    return HttpResponse('hello world')

def sample1(request):
    return HttpResponse('welcome to django')

def sampleinfo(request):
    #data={'name':'Raju','age':23,'city':'godavarikhani'}
    #return JsonResponse(data)
    #data=[2,3,4,5]
    #return JsonResponse(data,safe=False)
    data={'result':[2,3,4,5]}
    return JsonResponse(data)


def dynamicresponse(request):
    name=request.GET.get("name",'')
    return HttpResponse(f"hello {name}")


def add(request):
    num1=int(request.GET.get("num1",'0'))
    num2=int(request.GET.get("num2",'0'))
    result=num1+num2
    return HttpResponse(f"the addition of {num1} and {num2} is {result}")


def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status":"ok","db":"connected"})
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})

@csrf_exempt
def addStudent(request):
    print(request.method)
    if request.method =="POST":
        data=json.loads(request.body)
        student=Student.objects.create(name= data.get('name'),age=  data.get('age'),email=data.get('email'))

       
      
        
        return JsonResponse({"status":"success","id":student.id},status=200)
    return JsonResponse({"error":"use post method"},status=400)