# Generated by Django 2.2.4 on 2019-10-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factoids', '0002_factoid_is_fun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factoid',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]
