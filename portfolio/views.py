from portfolio.models import ProjectCard
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Print form data to console (for debugging purposes)
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        
        # Compose email
        email_subject = f"New contact form submission: {subject}"
        email_message = f"You have received a new message from your website contact form.\n\n" \
                        f"Name: {name}\n" \
                        f"Email: {email}\n" \
                        f"Subject: {subject}\n" \
                        f"Message:\n{message}"
        
        # Send email
        try:
            send_mail(
                email_subject,
                email_message,
                settings.EMAIL_HOST_USER,
                ['wendyachieng98@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'An error occurred while sending your message. Please try again later.')
            print(f"Error sending email: {str(e)}")  # Log the error
        
        return redirect('index')
    
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Compose email
        email_subject = f"New contact form submission: {subject}"
        email_message = f"You have received a new message from your website contact form.\n\n" \
                        f"Name: {name}\n" \
                        f"Email: {email}\n" \
                        f"Subject: {subject}\n" \
                        f"Message:\n{message}"
        
        # Send email
        try:
            send_mail(
                email_subject,
                email_message,
                settings.EMAIL_HOST_USER,
                ['wendyachieng98@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'An error occurred while sending your message. Please try again later.')
            print(f"Error sending email: {str(e)}")  # Log the error
        
        return redirect('contact')
    
    return render(request, 'contact.html')

def explore(request):
    projects = ProjectCard.objects.all()
    return render(request, 'explore.html', {'projects': projects})

def services(request):
    if request.method == 'POST':
        name = request.POST.get('services-name')
        email = request.POST.get('services-email')
        budget = request.POST.get('services-budget')
        project_description = request.POST.get('services-project-description')
        project_category = request.POST.get('services-project-category')
        estimated_timeline = request.POST.get('services-estimated-timeline')
        
        # Print form data to the terminal
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Budget: {budget}")
        print(f"Project Description: {project_description}")
        print(f"Project Category: {project_category}")
        print(f"Estimated Timeline: {estimated_timeline}")

        # Compose the email content
        email_subject = 'New Quotation Request'
        email_message = f"""
        Name: {name}
        Email: {email}
        Budget: {budget}
        Project Description: {project_description}
        Project Category: {project_category}
        Estimated Timeline: {estimated_timeline}
        """
        
        # Send the email
        try:
            send_mail(
                email_subject,
                email_message,
                settings.EMAIL_HOST_USER,
                ['wendyachieng98@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your quotation request has been sent successfully!')
        except Exception as e:
            messages.error(request, 'An error occurred while sending your message. Please try again later.')
            print(f"Error sending email: {str(e)}")  # Log the error

        # Redirect to the same form page to display the success message
        return redirect('services')  # Assuming 'services' is the name of the URL pattern

    return render(request, 'services.html')