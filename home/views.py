from django.shortcuts import render, redirect
from django.contrib import messages
from . models import PackageGallery, Package, Banner
from numpy import random
from django.core.mail import EmailMessage
from django.http import HttpResponse


def home(request):
    packages = Package.objects.all().order_by('id')
    ban = Banner.objects.all()
    
    ban_len = int(len(ban))
    ban_rand = random.randint(0,ban_len)
    ban_rand_obj = ban[ban_rand]
    
    pack_len = int(len(packages))
    pack_rand = random.randint(0,pack_len)
    pack_rand_obj = packages[pack_rand]

    # package_images = PackageGallery.objects.all().order_by('id')
    
    context = {
        'packages': packages,
        'package_image': pack_rand_obj,
        'ban': ban_rand_obj
    }
    return render(request, 'index.html',context)



def is_valid_email(email):
    # Basic email validation
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

def email_message(request):
    if request.method == 'POST':
        subject = request.POST.get('contactSubject', '')
        message = request.POST.get('contactMessage', '')
        sender_email = request.POST.get('contactEmail', '')

        # Basic form validation
        if not subject or not message or not sender_email:
            messages.warning(request,'Please fill in all the fields.')
            return redirect('home')

        if not is_valid_email(sender_email):
            messages.warning(request,'Invalid email address.')
            return redirect('home')
        
        if subject and message and sender_email:
            email = EmailMessage(
                subject,
                message,
                sender_email,
                ['maptourism.co@gmail.com'],  # Replace with your email address
                reply_to=[sender_email],
            )
            email.send()
            messages.warning(request,'Email sent successfully.')
            return redirect('home')
        else:
            messages.warning(request,'Please fill in all the fields.')
            return redirect('home')

    # return render(request, 'contact_form.html')
    return redirect('home')