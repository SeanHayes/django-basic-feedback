# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#Django imports
from django import template

#App imports
from ..forms import FeedbackForm

register = template.Library()

@register.inclusion_tag('feedback/widget.html', takes_context=True)
def feedback_widget(context):
    return {
        'user': context['user'],
        'form': FeedbackForm()
    }
