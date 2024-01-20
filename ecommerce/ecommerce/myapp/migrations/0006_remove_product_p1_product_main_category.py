# Generated by Django 4.2.6 on 2023-11-18 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_product_p1"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="p1",
        ),
        migrations.AddField(
            model_name="product",
            name="main_category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="myapp.main_category",
            ),
        ),
    ]