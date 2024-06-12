from django.conf import settings
from django.shortcuts import render, redirect
from .models import QuotationRequest
from django.contrib import messages
from core.models import Project
import logging
from django.core.mail import send_mail, BadHeaderError

logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'quotation':
            # Quotation form processing
            full_name = request.POST.get('full_name')
            email_address = request.POST.get('email_address')
            project_category = request.POST.get('project_category')
            budget_range = request.POST.get('budget_range')
            project_description = request.POST.get('project_description')
            timeline = request.POST.get('timeline')
            
            # Validate required fields
            if not all([full_name, email_address, project_category, budget_range, project_description, timeline]):
                messages.error(request, 'All fields are required. Please fill in the form completely.')
                return render(request, 'index.html')
            
            # Create and save the QuotationRequest object
            quotation = QuotationRequest(
                full_name=full_name,
                email_address=email_address,
                project_category=project_category,
                budget_range=budget_range,
                project_description=project_description,
                timeline=timeline
            )
            quotation.save()
            
            # Send confirmation email
            subject = 'New Quotation Request'
            message = f"""
            You have received a new quotation request.
            
            Full Name: {full_name}
            Email Address: {email_address}
            Project Category: {project_category}
            Budget Range: {budget_range}
            Project Description: {project_description}
            Timeline: {timeline}
            """
            from_email = 'wendyachieng98@gmail.com'
            recipient_list = [email_address]

            try:
                send_mail(subject, message, from_email, recipient_list)
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
                return redirect('index')
            except Exception as e:
                logger.error(f"Failed to send email: {e}")
                messages.error(request, 'Failed to send email. Please try again later.')
                return redirect('index')
            
            # Show success message and refresh the page
            messages.success(request, 'Your quotation request has been submitted successfully. We will get back to you soon!')
            return redirect('index')

        elif form_type == 'contact':
            # Contact form processing
            name = request.POST.get('name')
            last_name = request.POST.get('last-name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            # Validate required fields
            if not all([name, last_name, email, subject, message]):
                messages.error(request, 'All fields are required. Please fill in the form completely.')
                return render(request, 'index.html')

            # Send contact email
            full_message = f"""
            You have received a new message from {name} {last_name}.
            
            Email: {email}
            Subject: {subject}
            Message: {message}
            """
            from_email = 'wendyachieng98@gmail.com'
            recipient_list = [email]

            try:
                send_mail(subject, full_message, from_email, recipient_list)
            except BadHeaderError:
                messages.error(request, 'Invalid header found.')
                return redirect('index')
            except Exception as e:
                logger.error(f"Failed to send email: {e}")
                messages.error(request, 'Failed to send email. Please try again later.')
                return redirect('index')

            # Show success message and refresh the page
            messages.success(request, 'Your message has been sent successfully. We will get back to you soon!')
            return redirect('index')

    # This block runs when the page is first loaded (GET request)
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Combine first name and last name
        full_name = f"{first_name} {last_name}"

        # Create the email content
        email_subject = f"New Contact Form Submission: {subject}"
        email_message = f"Name: {full_name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                email_subject,
                email_message,
                email,  # From email (the user's email)
                [settings.DEFAULT_FROM_EMAIL],  # To email (your email)
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

        return redirect('contact')

    return render(request, 'contact.html')

def explore(request):
    projects = Project.objects.all()
    return render(request, 'explore.html', {'projects': projects})

def services (request):
    return render(request, 'services.html')