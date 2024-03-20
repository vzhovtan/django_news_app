from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

class TeamView(TemplateView):
    template_name = "team.html"

class ContactView(TemplateView):
    template_name = "contact.html"