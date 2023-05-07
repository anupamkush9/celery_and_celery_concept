import time
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add, mul, update_user
from .models import Customer


# Create your views here.
def Indexview(request):
    print("--------------------------------------")
    # print(add(45, 56).delay())  //Incorrect way of Adding task to celery.
    add.delay(45,89)
    print("mul::",mul.delay(45,89))
    print("++++++++brfore call add method++++++++++++=")
    return HttpResponse("<h1>Hello world</h1>")

def race_condition_view(request):
    customer = Customer.objects.all()[0]
    customer.balance = 5
    update_user.delay()
    time.sleep(13)
    customer.save()
    return HttpResponse("<h1>Hello world from race_condition_view</h1>")
