from django.shortcuts import render
from student import settings as constant
from student.models import School
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# Create your views here.
def school_list_by_place(request, contient='europe'):
    content = {}
    countrys = constant.LIST_COUNTRY[contient]
    full_name_country = [] 
    for country in countrys:
    	full_name_country.append(constant.COUNTRY_NAME[country])
        schools = School.objects.filter(country=country)
        if schools:
        	content[country] = schools
    content['countrys'] = full_name_country 
    return render(request, 'school.html', content)
  