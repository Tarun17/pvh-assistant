#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    PVH Digital Assistant backend API

"""


from setuptools import setup


setup(
    name='pvh-digital-assistant-backend',
    author='3PillarGlobal',
    author_email='',
    url='http://3pillarglobal.com',
    description="Restful API for PVH Digital Assistant Backend",
    long_description=__doc__,
    keywords="",
    test_suite='pvh_digital.tests.suite',
    platforms='any',
    install_requires=[
        'pytest',
        'Flask',
        'flask-restplus'
    ],
    packages=[
        'pvh_digital',
        'pvh_digital.api',
    ],
    include_package_data=True,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    zip_safe=False,
)



