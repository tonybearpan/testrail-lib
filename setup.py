#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

setup(name='testrail-library',
      version='0.0.8',
      keywords=('TestRail', 'TestRail API'),
      description='Python client library for TestRail APIs (http)',
      long_description='See https://github.com/JASON0916/testrail-library',
      license='MIT License',

      url='https://github.com/JASON0916/testrail-library',
      author='Jason CM',
      author_email='847671011@qq.com',

      packages=find_packages(),
      include_package_data=True,
      platforms='any',
      install_requires=['requests'],
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      )
