=====
Wauth
=====

Wauth is a simple Django app to login via ajax. This process is very common, which is why this app will allow you to build a small system login quickly.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "wauth" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'wauth',
      )

2. Include the polls URLconf in your project urls.py like this:

      url(r'^/', include('wauth.urls')),

3. Run `python manage.py syncdb` to create the wauth models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a wauth (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/ to participate in the wauth.

