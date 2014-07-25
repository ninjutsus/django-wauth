#Wauth

Wauth is a simple Django app to login via ajax. This process is very common, which is why this app will allow you to build a small aplication login quickly.

##Settings

1. Install:


    pip install https://github.com/ninjutsus/django-wauth/zipball/master

2. Include the polls URLconf in your project urls.py like this:


    url(r'^wauth/', include('wauth.urls')),

3. Visit http://127.0.0.1:8000/wauth to use the app.

##Quick start

###Modal:

First, extends:

    {% extends 'wauth/base-slim.html' %}
    
Then, there are two ways to do this:

**The first:**

    {% block content %}
        {% include 'wauth/nav.html' %}
        {% include 'wauth/modal.html' %}
    {% endblock %}

**The second:**

    {% block content %}
        {% if user.is_authenticated %}
            Bienvenido: {{ user.username }}<br>
            <li><a href="{% url 'auth_logout' %}">Logout</a></li>
        {% else %}
            <a href="#" data-reveal-id="loginModal">Login</a>
        {% endif %}
        
        {% include 'wauth/modal.html' %}
    {% endblock %}
    
###Login external

First, extends:

    {% extends 'wauth/login-external.html' %}
    
**Note:**
When the user is log in, **login external** redirect to */* raiz url


###Login Complete
    visit: http://127.0.0.1:8000/wauth
    
Your can build this:
 
    {% extends 'wauth/base.html' %}
    

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
    