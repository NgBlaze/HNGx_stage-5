from django.urls import path
from . import views

urlpatterns = [
    # Define a URL pattern for video upload (e.g., /upload/)
    path('upload/', views.handle_video_upload, name='upload_video'),

    # Define a URL pattern for video playback (e.g., /video/<video_id>/)
    path('video/<int:video_id>/', views.render_video_page, name='play_video'),
]
