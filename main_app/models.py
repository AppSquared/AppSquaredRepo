from django.db import models
from django.urls import reverse

# Create your models here.


class User(models.Model):
    email: models.EmailField(max_length=100)
    username: models.CharField(max_length=100)
    password: models.CharField(max_length=100)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('trough', kwargs={'user_id': self.id})


class Application(models.Model):

    date_applied = models.DateField()
    application_link = models.CharField(max_length=100)

    APPLIED = 'A'
    INTERVIEWED = 'I'
    REJECTED = 'R'
    APPLICATION_STATUS_CHOICES = [
        (APPLIED, 'Applied'),
        (INTERVIEWED, 'Interviewed'),
        (REJECTED, 'Rejected')
    ]

    application_status = models.CharField(
        max_length=1,
        choices=APPLICATION_STATUS_CHOICES,
        default=APPLICATION_STATUS_CHOICES[0][0]
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Current status for the position of {self.job_title}: {self.get_status_display()}.\n You applied on {self.date_applied}.\n "

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = 'date'


class Company(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.SlugField(max_length=15).blank = True
    address = models.CharField(max_length=100).blank = True
    website = models.CharField(max_length=100).blank = True

    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=100).blank = True
    name = models.CharField(max_length=100).blank = True
    phone_number = models.SlugField(max_length=15).blank = True
    email = models.CharField(max_length=100).blank = True
    notes = models.TextField(max_length=250).blank = True

    def __str__(self):
        if self.title and self.name:
            return f'Point of contact: {self.name}, {self.title}.'
        elif self.title and not self.name:
            return f'Point of contact: {self.title}.'
        elif self.name and not self.title:
            return f'Point of contact: {self.name}.'
        else:
            return f'No Point of Contact found!"'

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    application = models.ForeignKey(Application, on_delete=models.CASCADE)
