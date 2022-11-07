from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse


from .models import Application, User
from .forms import ApplicationForm
# Create your views here.


class Landing(TemplateView):
    template_name = 'main_app/landing.html'


class Home(TemplateView):
    template_name = 'main_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['applications'] = Application.objects.all()

        return context


class Detail(DetailView):
    model = Application
    template_name = 'applications/detail.html'


class ApplicationCreate(CreateView):
    model = Application
    fields = ['link', 'date_applied', 'status']
    template_name = "applications/new.html"
    success_url = "/home/"

    # def get_success_url(self):
    #     return reverse('main_app:home')


class ApplicationUpdate(UpdateView):
    model = Application
    fields = ['link', 'date_applied', 'status']
    template_name = "applications/update.html"
    success_url = "/applications/"

    def get_success_url(self):
        return reverse('main_app:detail', kwargs={'pk': self.object.pk})


class ApplicationDelete(DeleteView):
    model = Application
    template_name = "applications/delete.html"
    success_url = "/home/"


# def users_profile(request, user_id):
#     user = User.objects.get(id=user_id)
#     application_form = ApplicationForm
#     return render(request, 'users_profile.html', {'user': user, 'application_form': application_form})


# def applications_index(request):
#     applications = Application.objects.all()
#     return render(request, 'applications/index.html', {'applications': applications})
