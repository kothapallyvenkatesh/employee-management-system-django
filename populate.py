import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbvproject.settings') #from wsgi this created by so django donts know so import
import django
django.setup()

from testapp.models import Employee
from faker import Faker
from random import *
fake = Faker()
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=fake.name()
        fesal=randint(10000,20000)
        feadd=fake.city()
        emp_records=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feadd)

n=int(input("Enter no. of employees"))
populate(n)
print(f'{n} recordsinserted sucesfully')

