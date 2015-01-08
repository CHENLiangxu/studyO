from django.conf.urls import patterns, include, url
from django.contrib import admin
import student
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^school/(?P<contient>\w+)/$', 'student.views.school_list_by_place', name='school'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
