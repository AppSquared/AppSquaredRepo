from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = 'main_app'

urlpatterns = [
    path('', views.Landing.as_view(), name='landing'),
    path('home/', views.Home.as_view(), name='home'),
    path('applications/', views.Applications.as_view(), name='applications'),
    # path('applications/', views.applications_index, name='index'),
    # path('users/<int:user_id>/', views.users_profile, name='applications'),
    # path('applications/<int:application_id>/', views.applications_detail, name='detail'),
    # path('applications/create/', views.applicationCreate.as_view(), name='applications_create')
]
