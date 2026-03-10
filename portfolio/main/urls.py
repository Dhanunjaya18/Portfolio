from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_submit, name='contact_submit'),
    path('resume/download/', views.download_resume, name='download_resume'),
    path('api/projects/', views.projects_api, name='projects_api'),
]
