from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('geos/<geo>/', views.profile_list, name='profile_list'),
    path('se/<cec>/', views.profile_detail, name='profile_detail'),
    path('se/<cec>/edit/', views.edit_profile, name='edit_profile'),
]