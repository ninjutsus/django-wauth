from django.shortcuts import render
from django.views.generic import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.http import HttpResponse, HttpResponseRedirect
import json


class BaseView(TemplateView):
    template_name = 'wauth/base.html'


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        if request.is_ajax:
            username = request.POST['username']
            password = request.POST['password']
            external = request.POST['external']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    if external:
                        data = {'success': True, 'message': 'Login Success', 'redirect': True}
                    else:
                        data = {'success': True, 'message': 'Login Success', 'redirect': False}

                else:
                    data = {'success': False, 'message': 'User is not active', 'redirect': False}
            else:
                data = {'success': False, 'message': 'Wrong username and/or password', 'redirect': False}

            return HttpResponse(json.dumps(data), mimetype='application/json')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class LoginExternalView(View):
    template_name = "wauth/login-external.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'external': 'true'})
