from django.conf.urls import patterns, include, url
from django.contrib import admin
import student
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^place/(?P<para>\w+)/$', 'student.views.school_list_by_place', name='school'),
    url(r'^school/(?P<school_id>\d+)/$', 'student.views.school_detail', name='school_detail'),
    url(r'^student/(?P<student_id>\d+)/$', 'student.views.student_detail', name='student_detail'),
    url(r'^specialty/(?P<para>\w+)/$', 'student.views.specialty_list', name='specialty'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
