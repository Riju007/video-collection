"""Views for the app hall."""
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from halls.models import Hall, Video
from halls.forms import VideoForm, SearchForm


def home(request):
    """Home page view."""
    return render(request, "halls/home.html")


def dashboard(request):
    """Display a dashboard for the user."""
    return render(request, "halls/dashboard.html")


def add_video(request, pk):
    """Add video for hall of fame."""
    form = VideoForm()
    search_form = SearchForm()

    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            video = Video()
            video.url = form.cleaned_data['url']
            video.title = form.cleaned_data['title']
            video.youtube_id = form.cleaned_data['youtube_id']
            video.hall = Hall.objects.get(pk=pk)
            video.save()
            return redirect('home')

    context = {'form': form, 'search_form': search_form}
    return render(request, 'halls/add_video.html', context=context)


class SignUp(CreateView):
    """View for the user Sign Up functionality."""

    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


class CreateHall(CreateView):
    """Create a hall."""

    model = Hall
    fields = ["title"]
    template_name = "halls/create_hall.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        """Validate the form and save the data."""
        form.instance.user = self.request.user
        super(CreateHall, self).form_valid(form)
        return redirect("home")


class DetailHall(DetailView):
    """Details of a hall."""

    model = Hall
    template_name = "halls/detail_hall.html"


class UpdateHall(UpdateView):
    """Update a hall details."""

    model = Hall
    template_name = 'halls/update_hall.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')


class DeleteHall(DeleteView):
    """Delete a hall object."""

    model = Hall
    template_name = 'halls/delete_hall.html'
    success_url = reverse_lazy('dashboard')
