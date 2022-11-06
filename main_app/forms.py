from django.forms import ModelForm
from .models import Application


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['link', 'date_applied', 'status']
