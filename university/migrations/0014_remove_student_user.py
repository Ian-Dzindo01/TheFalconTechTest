# Generated by Django 5.0 on 2024-02-04 17:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("university", "0013_student_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="user",
        ),
    ]
