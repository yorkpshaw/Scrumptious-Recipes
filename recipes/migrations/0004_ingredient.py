# Generated by Django 4.1 on 2022-08-29 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0003_fooditem"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingredient",
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
                ("amount", models.FloatField()),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="recipes.fooditem",
                    ),
                ),
                (
                    "measure",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="recipes.measure",
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ingredients",
                        to="recipes.recipe",
                    ),
                ),
            ],
        ),
    ]
