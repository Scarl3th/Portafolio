from django.urls import path
from pages import views



urlpatterns = [
    path("", views.home, name='home'),
    path("aboutme",views.aboutme, name='aboutme'),
    path("education",views.education, name='education'),
    path("projects",views.projects,name='projects')
]