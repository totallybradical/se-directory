# Generated by Django 2.2.4 on 2019-08-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiletag',
            name='text',
            field=models.CharField(max_length=50),
        ),
    ]
