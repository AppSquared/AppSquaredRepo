from django.contrib import admin
from .models import Application, Position, Contact, Company

# Register your models here
admin.site.register(Application)
admin.site.register(Position)
admin.site.register(Contact)
admin.site.register(Company)
