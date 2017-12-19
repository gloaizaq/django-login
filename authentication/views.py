from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from authentication import forms
from django.contrib.auth import views, login, logout
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here.
class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = forms.LoginForm
    success_url =  reverse_lazy("authentication:welcome")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
             # return super(LoginView, self).dispatch(request, *args, **kwargs)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

class WelcomeTemplateView(TemplateView):
    template_name = 'authentication/welcome.html'
