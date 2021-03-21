from account.views import logout_view
from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
    path("login", LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout", logout_view, name="logout"),
]
