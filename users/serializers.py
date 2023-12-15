from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
import json

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    """validate the user credentials"""
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(
        label=_("Password"),
        write_only=True,
        style={'input_type': 'password'}
    )

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                refresh = RefreshToken.for_user(user)

                data = {
                    'username': user.username,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }
                return data
            else:
                raise AuthenticationFailed('Invalid credentials!')
        else:
            raise serializers.ValidationError('Username and password are required')

class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    # validation happens during entry this is for API
    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords must match.')
        return data

    def create(self, validated_data):
        """create and return a new user"""
        user = self.Meta.model.objects.create_user(
            id_number = validated_data['id_number'],
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password2']
        )
        return user

    class Meta:
        model = User
        fields = (
            'id', 'id_number', 'email', 'username',
            'password1', 'password2'
        )
        read_only_fields = ('id',)
