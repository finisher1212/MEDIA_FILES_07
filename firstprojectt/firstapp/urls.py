from django.urls import path
from . import views

urlpatterns = [
    path('',views.Homeview,name='home'),
    path('file/',views.Fileuploadview,name='file'),
    path('newfile/',views.model_form_upload,name='newfile'),
    path('showfile/',views.showfileview,name='showfile'),
]