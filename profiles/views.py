from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Create your views here.
from django.shortcuts import redirect
from .models import Profile
from factoids.models import Factoid
from .forms import ProfileForm
from django.http import JsonResponse

def profile_list(request):
    profiles = Profile.objects.order_by('name')
    return render(request, 'profile_list.html', {'profiles': profiles})

def profile_detail(request, id=None):
    profile = get_object_or_404(Profile, id=id)
    factoids = Factoid.objects.filter(profile=profile)
    return render(request, 'profile_detail.html', {'profile': profile, 'factoids': factoids})