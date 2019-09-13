from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Create your views here.
from django.shortcuts import redirect
from .models import Profile
from profile_tags.models import ProfileTag
from factoids.models import Factoid
from django.http import JsonResponse

def profile_list(request):
    profiles = Profile.objects.order_by('name')
    tags = ProfileTag.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles, 'tags': tags})

def profile_detail(request, id=None):
    profile = get_object_or_404(Profile, id=id)
    factoids = Factoid.objects.filter(profile=profile)
    return render(request, 'profile_detail.html', {'profile': profile, 'factoids': factoids})