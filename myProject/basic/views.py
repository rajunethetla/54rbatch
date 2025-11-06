from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

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
