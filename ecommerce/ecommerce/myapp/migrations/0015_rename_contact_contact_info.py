# Generated by Django 4.2.6 on 2023-12-09 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0014_contact"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="contact",
            new_name="contact_info",
        ),
    ]