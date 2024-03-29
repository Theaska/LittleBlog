from django.urls import reverse_lazy
from allauth.account.views import SignupView, LoginView, LogoutView
from .forms import MyLoginForm, MySignupForm, MySocialSignupForm
from django.contrib.auth import logout
from django.shortcuts import redirect, reverse

class MySignUp(SignupView):
    form_class = MySignupForm
    template_name = 'registration/signup.html'

class MyLoginView(LoginView):
    form_class = MyLoginForm
    template_name = 'registration/login.html'

def logout_view(request):
    logout(request)
    return redirect(reverse("myblog:index"))
