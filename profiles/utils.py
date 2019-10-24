from profiles.models import Profile
from django.contrib.auth.models import User

def create_default_profile(cec, name):
    user = django.contrib.auth.models.User.objects.get(username=cec)
    new_profile = profiles.models.Profile.objects.create(
        name=name,
        cec=cec,
        user=user.id,
        team="TEMP",
        region="O",
        primary_strength="UNK",
        secondary_strength="UNK"
    )
    new_profile.save()
