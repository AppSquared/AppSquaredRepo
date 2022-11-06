from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = 'main_app'

urlpatterns = [
    path('', views.Landing.as_view(), name='landing'),
    path('home/', views.Home.as_view(), name='home'),
    path('applications/<int:pk>/', views.Detail.as_view(), name='detail'),
    path('applications/new/', views.ApplicationCreate.as_view(),
         name='application_create'),
    path('applications/<int:pk>/update/',
         views.ApplicationUpdate.as_view(), name="application_update"),
    path('applications/<int:pk>/delete/',
         views.ApplicationDelete.as_view(), name="application_delete"),


    # path('users/<int:user_id>/', views.users_profile, name='applications'),
]
