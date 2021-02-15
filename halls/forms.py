"""forms for the app halls."""
from halls.models import Video
from django import forms


class VideoForm(forms.ModelForm):
    """Form for the video class."""

    class Meta:
        """Meta class for form."""

        model = Video
        fields = ['title', 'url', 'youtube_id']
        labels = {'youtube_id': 'YouTube ID'}


class SearchForm(forms.Form):
    """Search for a youtube video."""

    search_term = forms.CharField(max_length=255, label='Search for Videos: ')
