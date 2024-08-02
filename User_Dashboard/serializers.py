from rest_framework import serializers
from User.models import User


class UserProfileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]