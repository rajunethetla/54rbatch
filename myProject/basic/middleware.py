from django.http import JsonResponse
import re
import json
import jwt
from  django.conf import settings
from  basic.models import Users
class basicMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        #print(request,"hello")
        if(request.path=="/add/"):
            print(request.method,"method")
            print(request.path)
        response=self.get_response(request)
        return response
    
# import json
# class signupMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request):
#         data=json.loads(request.body)
#         username=data.get("username")
#         email=data.get("email")
#         dob=data.get("dob")
#         password=data.get("pswd")


class sscMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path in ["/job1/","/job2/"]):
            ssc_result=request.GET.get("ssc")
            print(ssc_result,'hello')
            if(ssc_result !='True'):
                return  JsonResponse({"error":"u should qualify atleast ssc to apply these job"},status=400)
        return  self.get_response(request)

class medicalfitMiddleware: 
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if(request.path == "/job1/"):
            medical_fit_result=(request.GET.get("medically_fit"))
            if(medical_fit_result !='True'):
                return JsonResponse({"error":"u not medically fit to apply for this job role"},status=400)
        return self.get_response(request)
        
class ageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if request.path in ["/job1/", "/job2/"]:
            age_checker = int(request.GET.get("age", 17))
            if age_checker < 18 or age_checker > 25:
                return JsonResponse({"error": "age must be between 18 and 25"}, status=400)
        return self.get_response(request)

       
        
class UsernameMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if (request.path == "/signup/"):
            data=json.loads(request.body)
            username=data.get("username","")
            if not username:
                return  JsonResponse({"error":"username is required"},status=400)
            if len(username)<3  or len(username)>20:
                return JsonResponse({"error":"username should contain 3 to 20 characters"},status=400)
            if username[0] in "._" or  username[-1]  in "._":
                return JsonResponse({"error":"username should not starts or ends with . or _"},status=400)
            if not re.match(r"^[a-zA-Z0-9._]+$",username):
                return  JsonResponse({"error":"usernname should contains letters,numbers,dot,underscore"},status=400)
            if ".."  in  username or "__" in username:
                return  JsonResponse({"error":"cannot have .. or  __"},status=400)
            
        return self.get_response(request)

class EmailMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if (request.path == "/signup/"):
            data=json.loads(request.body)
            email=data.get("email")
            if not email:
                return  JsonResponse({"error":"email should  nnot bbe empty"},status=400)
            email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
            if not re.match(email_pattern, email):
                return JsonResponse({"error": "invalid email format"}, status=400)
            if Users.objects.filter(email=email).exists():
                return JsonResponse({"error": "email already exists"}, status=400)

        return self.get_response(request)
    

class authenticate_middleware():
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if request.path=="/users/":
            token=request.headers.get("Authorization")
            print(token,"token")
            if not token:
                return JsonResponse({"error":"Authorization  token missing"},status=400)
            token_value=token.split(" ")[1]
            print(token_value,"token_value")
            try:
                decoded_data = jwt.decode(token_value,settings.SECRET_KEY,algorithms=["HS256"])
                print(decoded_data,"decoded_data")
                request.token_data=decoded_data
                
            except  jwt.ExpiredSignatureError:
                return JsonResponse({"error":"token is expired please login again"},status=400)
        return self.get_response(request)



    