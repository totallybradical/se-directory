from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Create your views here.
from django.shortcuts import redirect
from .models import Profile
from .forms import EditProfileForm
from profile_tags.models import ProfileTag
from factoids.models import Factoid
from django.http import JsonResponse

def profile_list(request):
    profiles = Profile.objects.exclude(geo="TEMP").exclude(team="TEMP").order_by('name')
    tags = ProfileTag.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles, 'tags': tags})

def profile_detail(request, cec=None):
    profile = Profile.objects.get(cec=cec)
    factoids = Factoid.objects.filter(profile=profile)
    return render(request, 'profile_detail.html', {'profile': profile, 'factoids': factoids})

def edit_profile(request, cec=None):
    profile_id = Profile.objects.get(user=request.user.id).id
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == "POST" and request.user.is_authenticated and request.user == profile.user:
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', cec=cec)
        else:
            print(form.errors)
    else:
        form = EditProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form, 'profile': profile})