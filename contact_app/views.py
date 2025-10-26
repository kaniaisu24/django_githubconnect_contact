
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us! We will get back to you soon.")
            return redirect('thank_you')
    else:
        form = ContactForm()
    return render(request, 'contact_app/contact.html', {'form': form})

def thank_you_view(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_app/thankyou.html', {'contacts': contacts})

