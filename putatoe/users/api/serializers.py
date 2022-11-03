from django.contrib.auth import get_user_model
from rest_framework import serializers
from putatoe.users.models import Data

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ["var"]