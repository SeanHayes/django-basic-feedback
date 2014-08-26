# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#Python imports
from datetime import datetime

#Django imports
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test.client import Client

#App imports
from ..models import Feedback

#Test imports
from .util import BaseTestCase

class FeedbackTestCase(BaseTestCase):
    def test_post_success(self):
        post_data = {
            'text': 'This is a test!'
        }
        
        self.assertEqual(Feedback.objects.count(), 0)
        
        response = self.client.post(reverse('feedback'), post_data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Feedback.objects.count(), 1)
        
        f = Feedback.objects.all()[0]
        self.assertEqual(f.user, self.user1)
        self.assertNotEqual(f.date, None)
        self.assertEqual(f.page, '')
        self.assertEqual(f.text, post_data['text'])
        self.assertEqual(f.archived, False)
        
