# Generated by Django 4.1.1 on 2022-10-04 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="skill",
            field=models.TextField(default="c", max_length=500),
        ),
    ]
