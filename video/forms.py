from django import forms
from .models import Video  # Import the Video model


class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']
