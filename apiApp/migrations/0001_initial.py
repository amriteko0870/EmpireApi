# Generated by Django 4.0.3 on 2022-03-10 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='storeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(max_length=100)),
                ('sales', models.CharField(max_length=100)),
                ('no_of_orders', models.CharField(max_length=100)),
                ('no_of_customers', models.CharField(max_length=100)),
            ],
        ),
    ]