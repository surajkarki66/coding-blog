from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):        # includes all default fields eg first_name, last_name, email, password, groups

        model = CustomUser

        fields = ('username', 'email', 'age',)  # Fields that are used in creating custom user





class CustomUserChangeForm(UserChangeForm):

     class Meta:

           model = CustomUser

           fields = ('username', 'email', 'age',)

