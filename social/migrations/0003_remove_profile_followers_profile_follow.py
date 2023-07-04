# Generated by Django 4.2.1 on 2023-07-04 12:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("social", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="followers",
        ),
        migrations.AddField(
            model_name="profile",
            name="follow",
            field=models.ManyToManyField(
                blank=True, related_name="follow", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
