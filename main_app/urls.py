from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('applications/<int:pk>/', views.application_detail, name='detail'),
    path('applications/create/', views.ApplicationCreate.as_view(),
         name='applications_create'),
    path('applications/<int:pk>/update/',
         views.ApplicationUpdate.as_view(), name="applications_update"),
    path('applications/<int:pk>/delete/',
         views.ApplicationDelete.as_view(), name="applications_delete"),
    path('accounts/signup/', views.signup, name='signup'),
]
