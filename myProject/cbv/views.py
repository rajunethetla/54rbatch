from django.shortcuts import render
from django.views  import View
from django.http import HttpResponse,JsonResponse
from django.utils.decorators import  method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import PaymentDetails

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class DemoClass(View):
    def get(self,request):
        #return HttpResponse("hello iam get method")
        return JsonResponse({"info":"get"})
    def post(self,request):
       #return HttpResponse("hello iam post method")
       return JsonResponse({"info":"post"})
    def put(self,request):
        #return HttpResponse("hello iam put method")
        return JsonResponse({"info":"put"})
    def delete(self,request):
        #return HttpResponse("hello iam delete method")
        return JsonResponse({"info":"delete"})
    


@method_decorator(csrf_exempt,name="dispatch")
class PaymentInfo(View):
    def post(self,request):
        try:
            data=json.loads(request.body)
            payment=PaymentDetails.objects.create(payment_status=data["status"],
            amount=data["amount"],payment_mode=data["mode"],
            user_email=data["email"],order_id=data["order_id"])
            return JsonResponse({'message':'posted successfully',"trasactionid":str(payment.transaction_id)},status=201)
        except Exception as e:
            return JsonResponse({"message":"error"},status=500)


