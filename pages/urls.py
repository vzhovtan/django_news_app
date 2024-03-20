from django.urls import path
from .views import HomePageView, TeamView, ContactView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("team/", TeamView.as_view(), name="team"),
    path("contact/", ContactView.as_view(), name="contact"),
]