# Generated by Django 5.0.7 on 2024-07-18 17:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hacks", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="writer",
            unique_together={("username", "twitter")},
        ),
    ]
