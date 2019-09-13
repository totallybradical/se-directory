from django.urls import path
from django.conf.urls import url, include

from . import views
from . import utils

urlpatterns = [
    path('random/', utils.random_factoid, name='random_factoid'),
    path('<int:id>/', views.factoid_detail, name='factoid_detail'),
]