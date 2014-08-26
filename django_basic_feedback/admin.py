# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#Python imports
import logging

#Django imports
from django.contrib import admin

#App imports
from .models import Feedback

logger = logging.getLogger(__name__)

class FeedbackAdmin(admin.ModelAdmin):
    list_filter = ['archived']
    readonly_fields = ['date', 'text', 'user', 'page']
    search_fields = ['page', 'user']
    list_display = ('user', 'date', 'page')
    
    def queryset(self, request):
        qs = super(FeedbackAdmin, self).queryset(request)
        if not request.GET.has_key('archived__exact'):
            qs = qs.filter(archived=False)
        return qs

admin.site.register(Feedback, FeedbackAdmin)

