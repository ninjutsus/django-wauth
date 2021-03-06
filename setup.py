import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
LICENSE = open(os.path.join(os.path.dirname(__file__), 'LICENSE')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-wauth',
    version='0.1.0',
    packages=['wauth'],
    include_package_data=True,
    license=LICENSE,
    description='A simple Django app to login via ajax',
    long_description=README,
    url='https://github.com/Ninjitsus/django-wauth.git',
    author='NinjaCoder',
    author_email='ninjacoding.co@gmail.com',
    install_requires=[
        "Django>=1.6",
        "argparse>=1.2.1",
        "wsgiref>=0.1.2",
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: GNU License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)