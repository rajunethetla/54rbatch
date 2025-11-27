from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import Student
from  basic.models import Users
from django.contrib.auth.hashers import make_password,check_password

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
    

    elif request.method =="GET":
        result=list(Student.objects.values())
        print(result)
        return JsonResponse({"status":"ok","data":result},status=200)
        # data=json.loads(request.body)
        # student_id=data.get("id")
        # try:
        #     student=Student.objects.get(id=student_id)
        #     result={"id":student.id,"name":"student.name","age":student.age,"email":student.email}
        #     return JsonResponse({"status":"ok","data":result},status=200)
        # except Student.DoesNotExist:
        #     return JsonResponse({"status":"error","message":"student not found"},status=404)

    
    

    elif request.method =="PUT":
        data=json.loads(request.body)
        ref_id=data.get("id")
        new_email=data.get("email")
        existing_student=Student.objects.get(id=ref_id)
        existing_student.email=new_email
        existing_student.save()
        updated_data=Student.objects.filter(id=ref_id).values().first()
        return JsonResponse({"status":"data updated successfully","updated_data":updated_data},status=200)
    

    elif request.method =="DELETE":
        data=json.loads(request.body)
        ref_id=data.get("id")
        get_deleting_data=Student.objects.filter(id=ref_id).values().first()
        to_be_delete=Student.objects.get(id=ref_id)
        to_be_delete.delete()
        return JsonResponse({"status":"success","message":"student data deleted successfully","deleted_data":get_deleting_data},status=200)
    return JsonResponse({"error":"use post method"},status=400)



def job1(request):
    return JsonResponse({"message":"u have successfully applied  for job1"},status=200)
def job2(request):
    return  JsonResponse({"message":"u have successfully applied for job2"},status=200)


@csrf_exempt
def signUp(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        user=Users.objects.create(
            username=data.get("username"),
            email=data.get("email"),
            password=make_password(data.get("password")))

        return JsonResponse({"status":"success"},status=200)

@csrf_exempt
def  login(request):
    if  request.method=="POST":
        data=request.POST
        print(data)
        username=data.get("username")
        password=data.get("password")
        try:
            user=Users.objects.get(username=username)
            if  check_password(password,user.password):
                return JsonResponse({"status":"successfully loggedin"},status=200)
            else:
                return  JsonResponse({"status":"failure","message":"invalid password"},status=400)
        except Users.DoesNotExist:
            return JsonResponse({"status":"failure","message":"user  nnot found"},status=400)

#check  password when  u forgottenn  the password


@csrf_exempt
def  check(request):
    hashed="pbkdf2_sha256$870000$2nRDM2ErFvvJXz4i1racdd$K8PK6EKWctGIdjVSA7mnszRdIKP+qSS3I8AO+Ghol1I="
    ipdata=request.POST
    print(ipdata)
    #hashed=make_password(ipdata.get("ip"))
    x=check_password(ipdata.get("ip"),hashed)
    print(x)
   
    return JsonResponse({"status":"success","data":x},status=200)


