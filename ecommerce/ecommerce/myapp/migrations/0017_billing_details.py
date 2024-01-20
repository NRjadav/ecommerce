# Generated by Django 4.1.3 on 2023-12-23 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_add_cart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='billing_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.IntegerField()),
                ('address_line', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('zipcode', models.IntegerField()),
            ],
        ),
    ]
