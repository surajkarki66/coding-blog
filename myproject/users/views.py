from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render
from .models import Contact



class SignUpView(CreateView):                     # Views for  Sign up page.

   form_class = CustomUserCreationForm

   success_url = reverse_lazy('login')

   template_name = 'users/signup.html'


def contact(request):
   if request.method == "POST":
      name = request.POST.get('name', '')
      email = request.POST.get('email', '')
      phone = request.POST.get('phone', '')
      desc = request.POST.get('desc', '')
      contact = Contact(name=name, email=email, phone=phone, desc=desc)
      contact.save()  # save it in database
   return render(request, 'users/contact.html')


