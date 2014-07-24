
#Wauth


Wauth is a simple Django app to login via ajax. This process is very common, which is why this app will allow you to build a small aplication login quickly.

##Settings

1. Install:

    pip install https://github.com/ninjutsus/django-wauth/zipball/master

2. Include the polls URLconf in your project urls.py like this:

    url(r'^wauth/', include('wauth.urls')),

3. Visit http://127.0.0.1:8000/wauth to use the app.

##Quick start

####Modal:

First, extends:

    {% extends 'wauth/modal.html' %}

Then, in _block_ _content_ add the links for _login_ or _logout_

    {% block content %}
        {% if user.is_authenticated %}
            Bienvenido: {{ user.username }}<br>
            <li><a href="{% url 'auth_logout' %}">Logout</a></li>
        {% else %}
            <a href="#" data-reveal-id="loginModal">Login</a>
        {% endif %}
    {% endblock %}
    
###Login external

First, extends:

    {% extends 'wauth/login_external.html' %}
    
    
**Note:**
When the user is logueado, **login external** redirect to */* raiz url


###Login Complete
    Visit: http://127.0.0.1:8000/wauth