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
    print("##"*500)
    customer = Customer.objects.all()[0]
    print("++"*500)
    print("inside race_condition_view ")
    print("race_condition_view customer.name",customer.name)
    print("race_condition_view customer.balance",customer.balance)
    customer.balance = 5
    # what ever change will update_user method will make all of them will be discarded
    # because lastly this view update code will run.
    # that's why old name and new balance = 5 will be updated.
    update_user.delay()
    time.sleep(13)
    customer.save()
    return HttpResponse("<h1>Hello world from race_condition_view</h1>")
