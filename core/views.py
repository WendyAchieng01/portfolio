from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"Message from {name} <{email}>:\n\n{message}"

        send_mail(
            subject="New Contact Form Message",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],  # where email should go
        )

        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")


def project1(request):
    return render(request, 'project-1.html')

def project2(request):
    return render(request, 'project-2.html')

def project3(request):
    return render(request, 'project-3.html')

def project4(request):
    return render(request, 'project-4.html')

def project5(request):
    return render(request, 'project-5.html')

def project6(request):
    return render(request, 'project-6.html')

def project7(request):
    return render(request, 'project-7.html')