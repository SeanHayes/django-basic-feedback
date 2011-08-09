# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

from django.conf.urls.defaults import *

urlpatterns = patterns('django_basic_feedback.views',
	url(r'^$', 'add', name="feedback"),
)
