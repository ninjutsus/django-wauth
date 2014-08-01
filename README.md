#Wauth

Wauth is a simple Django app to login via ajax. This process is very common, which is why this app will allow you to build a small aplication login quickly.

##Settings

1. Install:

        pip install https://github.com/ninjutsus/django-wauth/zipball/master

2. Include the wauth URLconf in your project urls.py like this:

        url(r'^wauth/', include('wauth.urls')),

3. Add "wauth" to your INSTALLED_APPS setting like this:  

        INSTALLED_APPS = (
            ...
            'wauth',
        )

4. Run `python manage.py syncdb`

5. Visit http://127.0.0.1:8000/wauth to use the app.

##Quick start

    {% extends 'wauth/base.html' %}
    
###Login external

First, extends:

    {% extends 'wauth/login-external.html' %}
    
**Note:**
When the user is log in, **login external** redirect to */* raiz url  
This can be useful for login redirecto in some login redirect decorator

    

####Helpers
You can use the following tags

For add content

    {% block content %}
    {% endblock %}
    
For add css files

    {% block extracss %}
    {% endblock %}

For add js files

    {% block extrajs %}
    {% endblock %}
    