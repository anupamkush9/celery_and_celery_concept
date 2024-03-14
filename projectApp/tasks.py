# Create your tasks here

from celery import shared_task
import time

from .models import Customer

@shared_task
def add(x, y):
    print("add mehtod is running =======================")
    print( x + y)
    return None


@shared_task
def mul(x, y):
    print(x*y)
    print("mul mehtod is running =======================")

    return x * y

@shared_task
def printing_msg():
    print("========printing msg===================")
    return None

@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def update_user():
    customer = Customer.objects.all()[0]
    print("inside update_user ")
    print("update_user customer.name",customer.name)
    print("update_user customer.balance",customer.balance)
    customer.name = "ghghjgjkkjh"
    print("user is updating............")
    customer.save()
    print("user updated............")