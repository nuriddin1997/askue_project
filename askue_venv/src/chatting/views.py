from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    template_name = "chatting/home.html"
    context = {
        "page_name": "ASKUE",
        "page_title": "Home",
    }
    if not request.user.id == None:
        return render(request, template_name, context)
    #     return redirect("login")
    # else:
    #     return render(request, template_name, context)
