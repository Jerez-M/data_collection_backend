from .models import FarmData
from rest_framework.serializers import ModelSerializer


class FarmDataSerializer(ModelSerializer):

    class Meta:
        model = FarmData
        exclude = ["date_created", "last_updated"]

        extra_kwargs = {
            "farmer_name": {"required": True},
            "national_id": {"required": True},
            "farm_type": {"required": True},
            "phone_number": {"required": True},
        }

class FarmDataRetrieveSerializer(ModelSerializer):

    class Meta:
        model = FarmData
        fields = "__all__"


class MinimizedFarmDataSerializer(ModelSerializer):
    class Meta:
        model = FarmData
        fields = ["id", "FarmData_name"]
