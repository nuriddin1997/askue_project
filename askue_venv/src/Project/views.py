from django.shortcuts import render


def welcome_page(request):
    template_name = "welcome.html"
    context = {
        "page_name": "Welcome",
        "page_title": "Welcome",
        "scroll": "Thanks to my father Nuriddin! He created me.",
    }
    return render(request, template_name, context)
