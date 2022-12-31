# Create your tasks here

from celery import shared_task


@shared_task
def add(x, y):
    print("add mehtod is running =======================")
    print( x + y)
    return None


@shared_task
def mul(x, y):
    print(x*y)
    return x * y

@shared_task
def printing_msg():
    print("========printing msg===================")
    return None

@shared_task
def xsum(numbers):
    return sum(numbers)

