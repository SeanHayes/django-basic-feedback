# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

try:
    from django.conf.urls import *
except ImportError: 
    from django.conf.urls.defaults import *

urlpatterns = patterns('django_basic_feedback.views',
	url(r'^$', 'add', name="feedback"),
)
