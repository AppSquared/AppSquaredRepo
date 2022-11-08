from django.forms import ModelForm
from .models import Application, User


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['link', 'date', 'status']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
