from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add, mul
# Create your views here.
def Indexview(request):
    print("--------------------------------------")
    # print(add(45, 56).delay())  //Incorrect way of Adding task to celery.
    add.delay(45,89)
    print("mul::",mul.delay(45,89))
    print("++++++++brfore call add method++++++++++++=")
    return HttpResponse("<h1>Hello world</h1>")