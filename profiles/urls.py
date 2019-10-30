from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('<geo>/', views.profile_list, name='profile_list'),
    path('<cec>/', views.profile_detail, name='profile_detail'),
    path('<cec>/edit/', views.edit_profile, name='edit_profile'),
]