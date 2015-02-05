from django.contrib import admin
from student.models import Student, School, Situation_school, Specialty
# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name_cn', 'country')

class StudentAdmin(admin.ModelAdmin):
	list_display = ('name_cn', 'telephone_protable')

class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name_cn', 'name_local')

class SituationSchoolAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'school_name', 'specialty_name')

admin.site.register(Student, StudentAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Situation_school, SituationSchoolAdmin)
admin.site.register(Specialty, SpecialtyAdmin)