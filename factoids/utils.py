from django.shortcuts import render
from django.db.models import Max
import random

from .models import Factoid
from .views import factoid_detail

def random_factoid(request):
    max_id = Factoid.objects.all().aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        factoid = Factoid.objects.filter(is_fun=True).filter(pk=pk).first()
        if factoid:
            return factoid_detail(request, pk)