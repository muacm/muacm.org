from django.shortcuts import render

# below for class based views
from django.views.generic import TemplateView
from acmapp.models import Event, Project, TeamMember, Blog


class HomePageView(TemplateView):
    template_name = "acmapp/home.html"

    def get(self, request, *args, **kwargs):

        # Contexts Dictionary
        context = {

        }

        return super(HomePageView, self).render_to_response(context)


class ProjectPageView(TemplateView):
    template_name = "acmapp/project.html"

    def get(self, request, *args, **kwargs):

        # Contexts Dictionary
        context = {
            "projects": Project.objects.all(),
        }

        return super(ProjectPageView, self).render_to_response(context)


class EventPageView(TemplateView):
    template_name = "acmapp/event.html"

    def get(self, request, *args, **kwargs):

        # Contexts Dictionary
        context = {
            "events": Event.objects.all(),
        }

        return super(EventPageView, self).render_to_response(context)


class TeamPageView(TemplateView):
    template_name = "acmapp/team.html"

    def get(self, request, *args, **kwargs):

        # Contexts Dictionary
        context = {
            "members": TeamMember.objects.all(),
        }

        return super(TeamPageView, self).render_to_response(context)

class ContactPageView(TemplateView):
    template_name = "acmapp/contact.html"

    def get(self, request, *args, **kwargs):

        # Contexts Dictionary
        context = {
        }

        return super(ContactPageView, self).render_to_response(context)


class BlogPageView(TemplateView):
    template_name = "acmapp/blog.html"

    def get(self, request, *args, **kwargs):

        # Contexts Dictionary
        context = {
            "blogs": Blog.objects.all(),
        }

        return super(BlogPageView, self).render_to_response(context)
