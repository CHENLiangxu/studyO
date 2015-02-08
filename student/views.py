# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404 
from student import settings as constant
from student.models import School, Student, Situation_school, Specialty
from django.template.defaulttags import register
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

#move to tools.py
def find_contient(country):
    if country in constant.LIST_COUNTRY_EUROPE:
        return 'europe'
    if country in constant.LIST_COUNTRY_ASIA:
        return 'asia'
    if country in constant.LIST_COUNTRY_AMERICAN:
        return 'amecian'
    if country == 'AU':
        return 'australia'

#register function for get item by the key
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# Create your views here.
def school_list_by_place(request, para='europe'):
    content = {}
    content['schools'] = {}
    countrys = constant.LIST_COUNTRY[para]
    full_name_country = [] 
    for country in countrys:
        full_name_country.append((country, constant.COUNTRY_NAME[country]))
        schools = School.objects.filter(country=country)
        if schools:
            content['schools'][country] = schools
    content['countrys'] = full_name_country 
    return render(request, 'school.html', content)

def school_detail(request, school_id):
    content = {}
    school = get_object_or_404(School, pk=school_id)
    content['contient'] = find_contient(school.country)
    if school:
        content['school'] = school
        #find all the student who study in this school
        situations = Situation_school.objects.filter(school=school_id)
        if situations:
            content['situations'] = situations
    return render(request, 'school_detail.html', content)

def student_detail(request, student_id):
    content = {}
    student = get_object_or_404(Student, pk=student_id)
    if student:
        content['student'] = student
        situations = Situation_school.objects.filter(student=student_id)
        #situations have too many information, maybe need to choice something important information
        if situations:
            content['situations'] = situations
        #to do situdations of student, education, project, cv, activity
    return render(request, 'student_detail.html', content)

def specialty_list(request, para=constant.ENGINEERING):
    content = {}
    specialtys = Specialty.objects.filter(specialty_type=para)
    content['specialtys'] = specialtys
    if specialtys:
        content['schools'] = {}
        for spe in specialtys:
            school_list = [] 
            situations = Situation_school.objects.filter(specialty=spe)
            if situations:
                school_list = list(set([situation.school for situation in situations]))
                content['schools'][spe.name_cn] = school_list
            else:
                content['schools'][spe.name_cn] = ''

    return render(request, 'specialty.html', content)