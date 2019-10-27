from django.urls import path
from django.conf.urls import url, include

from . import views
from . import utils

urlpatterns = [
    path('add/', views.add_factoid, name='add_factoid'),
    path('random/', utils.random_factoid, name='random_factoid'),
    path('user/', views.factoids_list, name='factoids_list'),
    path('<int:id>/', views.factoid_detail, name='factoid_detail'),
    path('<int:id>/delete/', views.delete_factoid, name='delete_factoid')
]