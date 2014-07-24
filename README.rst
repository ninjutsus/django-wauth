=====
Wauth
=====

Wauth is a simple Django app to login via ajax. This process is very common, which is why this app will allow you to build a small system login quickly.

Detailed documentation is in the "docs" directory.

Quick start
-----------
1. Install:

       pip install https://github.com/ninjutsus/django-wauth/archive/master.zip

2. Include the polls URLconf in your project urls.py like this:

      url(r'^wauth/', include('wauth.urls')),

3. Visit http://127.0.0.1:8000/wauth to use the app.

