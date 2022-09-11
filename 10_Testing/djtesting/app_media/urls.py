from django.urls import path
from app_media.views import upload_file, model_form_upload, upload_files

urlpatterns = [
    path('upload_file/', upload_file, name='upload_file'),
    path('upload_files/', upload_files, name='upload_files'),
    path('model_form_upload/', model_form_upload, name='model_form_upload'),
]