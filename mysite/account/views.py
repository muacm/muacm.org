# below 1 for logout
from django.contrib.auth import logout

# below 2 for allow access to views
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin

# django url shortcut
from django.shortcuts import redirect  # , render


@login_required
def logout_view(request):
    logout(request)
    return redirect("/")
