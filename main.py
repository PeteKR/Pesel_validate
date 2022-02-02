from random import randrange
import pandas as pd
from datetime import timedelta
from faker import Faker
fake = Faker('pl_PL')
Faker.seed(0)

def generate_unique_ssns(quantity,start2, end2,sex):
    start = pd.to_datetime(start2)
    end = pd.to_datetime(end2)
    delta = end - start
    series=[]
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    for _ in range(quantity):
        random_second = randrange(int_delta)
        series.append(fake.unique.pesel(date_of_birth=(start + timedelta(seconds=random_second)),sex=sex))
    return series

def validate_ssn(pesel,sex, date):
    IsPeselTrue=False
    sex_pesel=0
    if(sex=="K"):sex_pesel=0
    elif(sex=="M"): sex_pesel=1
    else:return False
    suma=(1*int(pesel[0]) + 3*int(pesel[1]) + 7*int(pesel[2]) + 9*int(pesel[3]) + 1*int(pesel[4]) +
          3*int(pesel[5]) + 7*int(pesel[6]) + 9*int(pesel[7]) + 1 * int(pesel[8]) + 3 * int(pesel[9]))
    if(10-suma%10==int(pesel[10])):
        if(int(pesel[9])%2==sex_pesel):
            x=date.split("-")
            x=int(x[0])
            month=int(pesel[2:4])
            if((month>=80 and month<=92) and (x%100==int(pesel[0:2]))):
                IsPeselTrue = True
            elif((month>=60 and month<=72) and (x%100==int(pesel[0:2]))):
                IsPeselTrue = True
            elif((month>=40 and month<=52) and (x%100==int(pesel[0:2]))):
                IsPeselTrue = True
            elif((month>=20 and month<=32) and (x%100==int(pesel[0:2]))):
                IsPeselTrue = True
            elif((month>=0 and month<=12) and (x%100==int(pesel[0:2]))):
                IsPeselTrue = True
    return IsPeselTrue

print(validate_ssn("00451676494","M","2100-05-16")) #True
print(validate_ssn("00451676494","K","2100-05-16")) #False
print(validate_ssn("03010157339","M","1903-01-01")) #True
print(validate_ssn("03010157339","K","1903-01-01")) #False
print(validate_ssn("02301681382","K","2002-10-16")) #True
print(validate_ssn("02301681382","M","2002-10-16")) #False