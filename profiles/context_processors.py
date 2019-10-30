from profiles.models import Profile

def user_profile(request):
    return {'user_profile': Profile.objects.filter(cec=request.user)}