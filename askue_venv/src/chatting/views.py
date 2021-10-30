from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    contact_names = User.objects.all()
    contact_counts = contact_names.count()
    print(contact_counts)
    template_name = "chatting/home.html"
    context = {
        "contact_counts": contact_counts,
        "contact_names": contact_names,
        "page_name": "ASKUE",
        "page_title": "Home",
    }

    if not request.user.id == None:
        return render(request, template_name, context)
    #     return redirect("login")
    # else:
    #     return render(request, template_name, context)
