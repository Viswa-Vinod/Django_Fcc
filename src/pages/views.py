from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contacts.html", {})

def about_view(request, *args, **kwargs):
    about_context = {
        "phone": "91-9686827656",
        "location": "bengaluru",
        "people": ["Vinod", "James", "Jonah", "Delsi"]
    }
    return render(request, "about.html", about_context)

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social</h1>")
