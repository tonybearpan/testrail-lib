#!/usr/bin/env python                                                                                                                                                
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

setup(name='testrail-library',
      version='0.0.1',
      keywords=('TestRail', 'TestRail API'),
      description='Python client library for TestRail APIs (http)',
      long_description='See http://liluo.github.com/douban-client',
      license='MIT License',

      url='http://liluo.github.com/douban-client',
      author='liluo',
      author_email='i@liluo.org',

      packages=find_packages(),
      include_package_data=True,
      platforms='any',
      install_requires=['py-oauth2>=0.0.8', 'six>=1.4.1'],
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],)