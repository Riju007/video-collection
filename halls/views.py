from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


def home(request):
    """Home page view."""
    return render(request, 'halls/home.html')


class SignUp(CreateView):
    """View for the user Sign Up functionality."""

    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'
