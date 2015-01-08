# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404 
from student import settings as constant
from student.models import School, Student, Situation_school
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
    if country == 'EN':
        return 'United Kingdom'

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
    print content['contient']
    if school:
        content['school'] = school
        #find all the student who study in this school
        situations = Situation_school.objects.filter(school=school_id)
        if situations:
            print situations
            content['situations'] = situations
    return render(request, 'school_detail.html', content)
