# Generated by Django 4.2.6 on 2023-11-25 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="color",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="myapp.color",
            ),
        ),
    ]
