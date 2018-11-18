# -*- coding:utf-8 -*-
from django.conf.urls import  url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^tasks/$', views.task_list, name='task_list'),
    # url(r'^tasks/$', views.TaskList.as_view(), name='task_list'),
    # url(r'^tasks/$', views.TaskListCreate.as_view(), name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),
    url(r'rlsinfo/$', views.rlsinfo_list, name='rlsinfo_list'),
    url(r'^rlsinfo/(?P<pk>[0-9]+)$',views.rlsinfo_detail, name='rlsinfo_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)