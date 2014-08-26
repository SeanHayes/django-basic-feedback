# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#Django imports
from django.contrib.auth.models import User
from django.test import TestCase

#App imports

class BaseTestCase(TestCase):
    def setUp(self):
        #setup users
        self.username = 'test_user'
        self.password = 'foobar'
        self.user1 = User.objects.create_user(self.username, 'test_user1@example.com', self.password)
        
        self.client.login(username=self.username, password=self.password)
