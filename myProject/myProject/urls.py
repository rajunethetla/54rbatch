"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from basic.views import sample
from basic.views import sample1
from basic.views import sampleinfo
from basic.views import dynamicresponse
from basic.views import add
from basic.views import health
from basic.views import addStudent
from basic.views import job1
from basic.views import job2
from basic.views import signUp,check,login,getAllUsers,home,aboutus,welcome,contact,services,projects
from basic2.views import bs2,productById,productBycategory
from cbv.views  import DemoClass,PaymentInfo


urlpatterns = [
    path('pay/',PaymentInfo.as_view()),
    path('cbv/',DemoClass.as_view()),
    path('product/<int:id>',productById),
    path('product/category/<str:ctg>',productBycategory),
    path('admin/', admin.site.urls),
    path('greet/',sample),
    path('54r/',sample1),
    path('info/',sampleinfo),
    path('response/',dynamicresponse),
    path('addition/',add),
    path('health/',health),
    path('add/',addStudent),
    path('job1/',job1),
    path('job2/',job2),
    path('signup/',signUp),
    path('check/',check),
    path('login/',login),
    path('users/',getAllUsers),
    path('home/',home,name='home'),
    path('about/',aboutus,name='about'),
    path('welcome/',welcome,name='welcome'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('projects/',projects,name='projects'),
    path('bs2/',bs2)
    

]
