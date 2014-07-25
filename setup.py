#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import django_basic_feedback

package_name = 'django_basic_feedback'
test_package_name = '%s_test_project' % package_name

setup(name='django-basic-feedback',
	version=django_basic_feedback.__version__,
	description="Provides a Feedback button on your pages and lets you view feedback via Django's admin site. Requires jQuery.",
	author='Seán Hayes',
	author_email='sean@seanhayes.name',
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Framework :: Django",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: GNU General Public License (GPL)",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.6",
		"Topic :: Internet :: WWW/HTTP :: Dynamic Content",
		"Topic :: Internet :: WWW/HTTP :: Site Management",
		"Topic :: Software Development :: Libraries",
		"Topic :: Software Development :: Libraries :: Python Modules"
	],
	keywords='django feedback widget',
	url='http://seanhayes.name/',
	download_url='https://github.com/SeanHayes/django-basic-feedback',
	license='BSD',
	packages=[
		'django_basic_feedback',
		'django_basic_feedback.templatetags',
		'django_basic_feedback.tests',
		'django_basic_feedback_test_project',
	],
	package_data={'django_basic_feedback': [
		'django_basic_feedback/templates/feedback/*',
		'django_basic_feedback/static/*',
	]},
	include_package_data=True,
	install_requires=['Django>=1.6',],
    test_suite = '%s.runtests.runtests' % test_package_name,
)

