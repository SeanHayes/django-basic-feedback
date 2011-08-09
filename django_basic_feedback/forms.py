# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#Django imports
from django import forms

#App imports
from models import Feedback

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ('text',)
