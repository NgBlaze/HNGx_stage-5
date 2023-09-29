from django.urls import path
from . import views  # Import views from your 'video' app

urlpatterns = [
    # Define a URL pattern for video upload (e.g., /upload/)
    path('upload/', views.upload_video, name='upload_video'),

    # Define a URL pattern for video playback (e.g., /video/<video_id>/)
    path('video/<int:video_id>/', views.play_video, name='play_video'),
]
