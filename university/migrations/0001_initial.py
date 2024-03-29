# Generated by Django 5.0 on 2024-01-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fName", models.CharField(max_length=50)),
                ("lName", models.CharField(max_length=50)),
                ("number", models.PositiveIntegerField()),
                ("email", models.EmailField(max_length=100)),
                ("smijerOdab", models.CharField(max_length=50)),
                ("skola", models.CharField(max_length=50)),
                ("prosjekOc", models.FloatField()),
                ("maturaOc", models.FloatField()),
                ("datumRodj", models.DateField()),
                ("mjestoRodj", models.CharField(max_length=100)),
                ("molbaUpis", models.CharField(max_length=500)),
            ],
        ),
    ]
