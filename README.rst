=====================
django-basic-feedback
=====================

.. image:: https://travis-ci.org/SeanHayes/django-basic-feedback.svg?branch=master
    :target: https://travis-ci.org/SeanHayes/django-basic-feedback
.. image:: https://coveralls.io/repos/SeanHayes/django-basic-feedback/badge.png?branch=master
    :target: https://coveralls.io/r/SeanHayes/django-basic-feedback?branch=master

Install
-------

1. Add 'django_basic_feedback' to INSTALLED_APPS.

2. Add '(r'^feedback/', include('django_basic_feedback.urls')),' to your root URL conf.

3. Put the following in your template's <head> tag (need to run './manage.py collectstatic'):
	<link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}feedback.css" />
	<script type="text/javascript" src="{{ STATIC_URL }}feedback.js"></script>

4. Put the following in the body of your template:
	{% load feedback_widget %}
	{% feedback_widget %}

5. Run './manager.py syncdb'.
