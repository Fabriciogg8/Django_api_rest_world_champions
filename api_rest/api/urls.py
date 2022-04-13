from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("teams/", views.TeamsView.as_view(), name="teams"),
    path("teams/<int:id>", views.TeamsView.as_view(), name="individual_team"),
]