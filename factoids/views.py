from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Create your views here.
from django.shortcuts import redirect
from .models import Factoid
from profiles.models import Profile
from django.http import JsonResponse

def factoid_detail(request, id=None):
    factoid = get_object_or_404(Factoid, id=id)
    return render(request, 'factoid_detail.html', {'factoid': factoid})