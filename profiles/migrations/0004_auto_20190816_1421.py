# Generated by Django 2.2.4 on 2019-08-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_cec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.CharField(choices=[('C', 'Central'), ('S', 'South'), ('E', 'East'), ('W', 'West')], max_length=1),
        ),
    ]
