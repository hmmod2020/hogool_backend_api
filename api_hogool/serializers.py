from rest_framework import serializers
from .models import *


class Farmer_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=FarmerInfo
        fields='__all__'

class Investor_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=InvestorInfo
        fields='__all__'

class News_Serializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields='__all__'

class Land_Serializer(serializers.ModelSerializer):
    class Meta:
        model=land
        fields='__all__'

class Crop_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Crops
        fields='__all__'