from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Application, User
from .forms import ApplicationForm
# Create your views here.


class Landing(TemplateView):
    template_name = 'main_app/landing.html'


class Home(TemplateView):
    template_name = 'main_app/home.html'

# ::DUMMY APPS FOR TESTING PURPOSES::
# :: DELETE THIS WHEN DB IS ACCESSIBLE FOR EVERYONE::


# class Application:
#     def __init__(self, link, date_applied, logged):
#         self.link = link,
#         self.date_applied = date_applied
#         self.logged = logged


# dummyAppList = [
#     Application("http://www.google.com", "2022-11-03", "today"),
#     Application("http://www.github.com", "2022-10-13",
#                 "10,000 years in the future"),
#     Application("http://www.amazon.com", "2022-12-23", "every christmas past"),
# ]


class Applications(TemplateView):
    template_name = 'applications/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['applications'] = Application.objects.all()
        # return context


# def users_profile(request, user_id):
#     user = User.objects.get(id=user_id)
#     application_form = ApplicationForm
#     return render(request, 'users_profile.html', {'user': user, 'application_form': application_form})


# def applications_index(request):
#     applications = Application.objects.all()
#     return render(request, 'applications/index.html', {'applications': applications})
