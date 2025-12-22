from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def bs2(request):
    return  JsonResponse({"data":"hello  iam from basic2"})


products = [
    {
        "id": 201,
        "name": "Sofa Set",
        "category": "Living Room",
        "price": 29999,
        "stock": 10,
        "rating": 4.6
    },
    {
        "id": 202,
        "name": "Office Chair",
        "category": "Office",
        "price": 8999,
        "stock": 25,
        "rating": 4.3
    },
    {
        "id": 203,
        "name": "Double Bed",
        "category": "Bedroom",
        "price": 27999,
        "stock": 6,
        "rating": 4.7
    },
    {
        "id": 204,
        "name": "Dining Table",
        "category": "Dining",
        "price": 21999,
        "stock": 8,
        "rating": 4.5
    },
    {
        "id": 205,
        "name": "Bookshelf",
        "category": "Decor",
        "price": 6499,
        "stock": 20,
        "rating": 4.2
    }
]

def productById(request,id):
    for  product in  products:
        if  product["id"]==id:
            return JsonResponse(product)
    return JsonResponse({"error":"product nnot   found"})
    

def productBycategory(request,ctg):
    for  product in  products:
        if  product["category"].lower()==ctg.lower():
            return JsonResponse(product)
    return JsonResponse({"error":"product nnot   found"})
