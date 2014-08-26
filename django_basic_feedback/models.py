# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#Python imports
from datetime import datetime

#Django imports
from django.conf import settings
from django.db import models

class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateTimeField(auto_now_add=True)
    page = models.CharField(max_length="255", blank=True)
    text = models.TextField()
    archived = models.BooleanField(default=False)

