# Generated by Django 4.1 on 2022-08-29 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0004_ingredient"),
    ]

    operations = [
        migrations.CreateModel(
            name="Step",
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
                ("order", models.IntegerField()),
                ("directions", models.CharField(max_length=300)),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="steps",
                        to="recipes.recipe",
                    ),
                ),
            ],
        ),
    ]
