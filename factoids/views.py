from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Create your views here.
from django.shortcuts import redirect
from .models import Factoid
from .forms import FactoidForm
from profiles.models import Profile
from django.http import JsonResponse

def factoids_list(request):
    user_profile = Profile.objects.get(user=request.user)
    user_factoids = Factoid.objects.filter(profile=user_profile)
    return render(request, 'factoids_list.html', {'user_factoids': user_factoids})

def factoid_detail(request, id=None):
    factoid = get_object_or_404(Factoid, id=id)
    return render(request, 'factoid_detail.html', {'factoid': factoid})

def add_factoid(request):
    if request.method == "POST":
        form = FactoidForm(request.POST)
        if form.is_valid():
            factoid = form.save(commit=False)
            user_profile = Profile.objects.get(user=request.user)
            factoid.profile = user_profile
            factoid.save()
            return redirect('factoids_list')
    else:
        form = FactoidForm()
    return render(request, 'add_factoid.html', {'form': form})

def delete_factoid(request, id=None):
    user_factoid = get_object_or_404(Factoid, id=id)
    factoid_profile = user_factoid.profile
    if request.method == "POST" and request.user.is_authenticated and request.user == factoid_profile.user:
        user_factoid.delete()
        messages.success(request, "Fact successfully deleted!")
        return redirect('factoids_list')
    
    context= {'user_factoid': user_factoid,
              'factoid_profile': factoid_profile,
              }
    
    return render(request, 'delete_factoid.html', context)    

