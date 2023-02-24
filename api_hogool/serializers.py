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

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class UserInfo_Serializer(serializers.ModelSerializer):
    class Meta:
        model=UserInfo
        fields='__all__'

class CropFarmer_Serializer(serializers.ModelSerializer):
    class Meta:
        model=FarmerCrops
        fields='__all__'

class Offer_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=InvestmentOffers
        fields='__all__'

class Orerd_land_rent_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrerdLandRent
        fields='__all__'

class jobs__infoSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderJob
        fields='__all__'



