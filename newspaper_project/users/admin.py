from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Contact


class CustomUserAdmin(UserAdmin):

     add_form = CustomUserCreationForm      # Add the custom user form from forms.py

     form = CustomUserChangeForm

     model = CustomUser

     list_display = ['email', 'username', 'age', 'is_staff', ]




admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Contact)


