import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsproject.settings')
import django
django.setup()
from faker import Faker
from random import *
from jobsapp.models import *
fake = Faker()
def phonenumbergen():
    d1 = randint(7,9)
    num = ''+str(d1)
    for i in range(9):
        num = num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany= fake.company()
        ftitle= fake.random_element(elements=('Project Manager','Teamlead','Software Engineer'))
        feligibility = fake.random_element(elements=("B.Tech","M.Tech","MCA"))
        faddress= fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        hydjobs_record = Noidajobsinfo.objects.get_or_create(Date=fdate,Company=fcompany,Title=ftitle,Eligibility=feligibility,Address=faddress,Email=femail,PhoneNumber=fphonenumber)
populate(25)
