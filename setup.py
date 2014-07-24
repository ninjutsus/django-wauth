import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
LICENCE = open(os.path.join(os.path.dirname(__file__), 'LICENCE')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-wauth',
    version='0.1.0',
    packages=['wauth'],
    include_package_data=True,
    license=LICENCE,
    description='A simple Django app to login via ajax',
    long_description=README,
    url='github.com/wils0n/django-wauth',
    author='wils0n',
    author_email='wiljm0.0@gmail.com',
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