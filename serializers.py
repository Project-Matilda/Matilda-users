# users/serializers.py

from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import AccessToken  # Import AccessToken for token generation

User = get_user_model()

# users/serializers.py

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all()), validate_email]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords don't match."})
        return attrs

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user  # Return the User instance directly



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False)  # Token is now optional for login

    class Meta:
        fields = ('username', 'password', 'token')

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError('Invalid username or password')
        
        # Check if token is provided and valid (if required)
        if 'token' in attrs and attrs['token']:
            try:
                AccessToken(attrs['token'])  # Validate the token
            except Exception:
                raise serializers.ValidationError('Invalid token')
        
        attrs['user'] = user  # Store user for further use
        return attrs
