from rest_framework import serializers
from accounts.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user_profile = UserProfile.objects.create_user(**validated_data)
        return user_profile

    class Meta:
        model = UserProfile
        fields = "__all__"
