import logging

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

logger = logging.getLogger('dashboard')


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            logger.info(f"New user registered: {user.username}")
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, "dashboard/signup.html", {"form": form})
