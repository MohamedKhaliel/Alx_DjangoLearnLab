from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        User = get_user_model()
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user