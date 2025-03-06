from django.db import models

# Create your models here.

class FarmData(models.Model):
    FARM_TYPES = (
        ("SMALL_SCALE", "Small Scale"),
        ("LARGE_SCALE", "Large Scale"),
        ("COMMERCIAL", "Commercial"),
        ("SUBSISTENCE", "Subsistence"),
    )
    CROPS = (
        ("MAIZE", "Maize"),
        ("WHEAT", "Wheat"),
        ("RICE", "Rice"),
        ("SOYBEAN", "Soybean"),
        ("COTTON", "Cotton"),
        ("TOBACCO", "Tobacco"),
        ("OTHER", "Other"),
    )

    farmer_name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=20, unique=True)
    farm_type = models.CharField(max_length=50, choices=FARM_TYPES)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    crop = models.CharField(max_length=50, choices=CROPS, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    farm_size = models.FloatField(blank=True, null=True, help_text="Size of the farm in hectares")
    irrigation_available = models.BooleanField(default=False, blank=True, null=True)
    soil_type = models.CharField(max_length=100, blank=True, null=True)
    average_yield = models.FloatField(blank=True, null=True, help_text="Average yield per hectare")
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.farmer_name} - {self.national_id}"