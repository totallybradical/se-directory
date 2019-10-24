def create_default_profile(cec, name):
    user = User.objects.get(username=cec)
    new_profile = Profile.objects.create(
        name=name,
        cec=cec,
        user=user.id,
        team="TEMP",
        region="O",
        primary_strength="UNK",
        secondary_strength="UNK"
    )
    new_profile.save()
