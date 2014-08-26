#!/usr/bin/env python
import os, sys
from . import settings
import django
from django.core.management import call_command

os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings' % settings.PROJECT_MODULE
sys.path.insert(0, settings.PROJECT_PARENT_DIR)

def runtests():
    try:
        django.setup()
    except AttributeError:
        pass
    
    call_command('test')
    sys.exit()

if __name__ == '__main__':
    runtests()
