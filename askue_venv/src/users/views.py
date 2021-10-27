from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"New account created successfully for {username}"
            )
            return redirect("login")
    else:
        form = RegisterForm()
    template_name = "users/signup.html"
    context = {
        "page_name": "Sign Up",
        "page_title": "Account Creation",
        "form": form,
    }
    return render(request, template_name, context)


@login_required
def profile(request):
    template_name = "users/profile.html"
    context = {
        "page_name": f"{request.user.username}'s Profile",
        "page_title": f"Profile-{request.user.username}",
    }
    return render(request, template_name, context)
