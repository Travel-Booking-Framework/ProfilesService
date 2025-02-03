from rest_framework import serializers
from Profile.models import UserProfile, UserBankInfo


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserBankInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBankInfo
        fields = '__all__'