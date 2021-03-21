from django.urls import path

from acmapp.views import (
    HomePageView,
    TeamPageView,
    EventPageView,
    ProjectPageView,
    ContactPageView,
    BlogPageView,
)

# from django.conf import settings

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("team", TeamPageView.as_view(), name="team-page"),
    path("events", EventPageView.as_view(), name="event-page"),
    path("projects", ProjectPageView.as_view(), name="project-page"),
    path("contact-us", ContactPageView.as_view(), name="contact-page"),
    path("blogs", BlogPageView.as_view(), name="blog-page"),
]
