# Generated by Django 5.0.3 on 2024-03-10 20:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
