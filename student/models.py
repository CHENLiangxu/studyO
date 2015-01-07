# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

#move to the setting.py
FRESHMAN = 'FR'
SOPHOMORE = 'SO'
JUNIOR = 'JR'
SENIOR = 'SR'
Master = 'M'
Doctor = 'PHD' 

YEAR_IN_SCHOOL_CHOICES = (
    (FRESHMAN, 'Freshman'),
    (SOPHOMORE, 'Sophomore'),
    (JUNIOR, 'Junior'),
    (SENIOR, 'Senior'),
    (Master, 'Master'),
    (Doctor, 'Doctor'),
)

# gender : true: man; false: woman; 
GENDER = (
    (True, 'man'),
    (False, 'woman'),
)

#country:
COUNTRY_CHOICES = (
    ('FR', 'France'),
    ('EN', 'United Kiongdom'),
    ('AU', 'Australia'),
    ('CA', 'Canada'),
    ('CH', 'Switzerland'),
    ('DE', 'Germany'),
    ('ES', 'Spain'),
    ('KR', 'Korea'),
    ('SG', 'Singapore'),
    ('JP', 'Japan'),
    ('IT', 'Italy'),
    ('US', 'United States'),
)
######################################

class Student(models.Model):
    user= models.OneToOneField(User)
    name_cn = models.CharField(max_length=30, default='')
    telephone_protable = models.CharField(max_length=16)
    adress = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=30, default='China')
    city = models.CharField(max_length=50, null=True)
    code_postal = models.CharField(max_length=10, null=True)
    gender = models. BooleanField(choices=GENDER, default=True)
    date_naissance = models.DateField(null=True)
    year_in_school = models.CharField(max_length=3,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=FRESHMAN)
    qq_link = models.CharField(max_length=30, null=True)
    site = models.URLField(null=True)
    facebook_link = models.URLField(null=True)


#situation of education
#one student has many situations(he has studied in many univercities)
class Situation_school(models.Model):
    date_end = models.DateField(null=True)
    date_start = models.DateField()
    specialty = models.ForeignKey('Specialty')
    school = models.ForeignKey('School')
    student = models.ForeignKey('Student')
    is_end = models.BooleanField(default=True)
    #do you want to publish in the CV
    is_pub = models.BooleanField(default=True)


class School(models.Model):
    name_local = models.CharField(max_length=200, null=True)
    name_cn = models.CharField(max_length=200)
    adress = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=2,
                               choices=COUNTRY_CHOICES,
                               null=True)
    city = models.CharField(max_length=50, null=True)
    code_postal = models.CharField(max_length=10, null=True)
    site = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=False)
    detail = models.TextField()

class Specialty(models.Model):
    name_local = models.CharField(max_length=200)
    name_cn = models.CharField(max_length=200)
    detail = models.TextField()




