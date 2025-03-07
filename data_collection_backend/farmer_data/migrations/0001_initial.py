# Generated by Django 5.1.6 on 2025-03-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(max_length=255)),
                ('national_id', models.CharField(max_length=20, unique=True)),
                ('farm_type', models.CharField(choices=[('SMALL_SCALE', 'Small Scale'), ('LARGE_SCALE', 'Large Scale'), ('COMMERCIAL', 'Commercial'), ('SUBSISTENCE', 'Subsistence')], max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=25, null=True)),
                ('crop', models.CharField(blank=True, choices=[('MAIZE', 'Maize'), ('WHEAT', 'Wheat'), ('RICE', 'Rice'), ('SOYBEAN', 'Soybean'), ('COTTON', 'Cotton'), ('TOBACCO', 'Tobacco'), ('OTHER', 'Other')], max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('farm_size', models.FloatField(blank=True, help_text='Size of the farm in hectares', null=True)),
                ('irrigation_available', models.BooleanField(blank=True, default=False, null=True)),
                ('soil_type', models.CharField(blank=True, max_length=100, null=True)),
                ('average_yield', models.FloatField(blank=True, help_text='Average yield per hectare', null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
