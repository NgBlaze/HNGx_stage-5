from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video
from .forms import VideoUploadForm


def render_video_page(request, video_id):
    try:
        # Logic to retrieve the video from the database
        video = Video.objects.get(pk=video_id)

        # Render the video playback page with the video data
        return render(request, 'video/play_video.html', {'video': video})
    except Video.DoesNotExist:
        return HttpResponse("Video not found", status=404)


def handle_video_upload(request):
    if request.method == 'POST':
        # Process the uploaded video file
        form = VideoUploadForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the video to the server's disk
            video = form.save()

            # Optionally, you can also save video metadata to a database

            # Redirect to the video playback page
            return redirect('play_video', video_id=video.id)

    else:
        # Display the video upload form
        form = VideoUploadForm()

    return render(request, 'video/upload_video.html', {'form': form})
