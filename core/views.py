from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


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