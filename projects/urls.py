from django.urls import path
from .views import projects, project, createProject

urlpatterns = [
    path("", projects, name="projects"),
    # path("project/(?P<pk>[\w-]+)/$", project, name="project"),
    path('project/<str:pk>', project, name="project"),

    path('create-project/', createProject, name="create-project")
]
