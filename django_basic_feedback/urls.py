# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

try:
    from django.conf.urls import *
except ImportError: 
    from django.conf.urls.defaults import *

from django_basic_feedback.views import add

urlpatterns = patterns('',
    url(r'^$', add, name="feedback"),
)
