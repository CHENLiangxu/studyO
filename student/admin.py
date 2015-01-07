from django.contrib import admin
from student.models import Student, School, Situation_school, Specialty
# Register your models here.
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Situation_school)
admin.site.register(Specialty)