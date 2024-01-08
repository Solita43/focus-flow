from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import UserAccount
from django.contrib.auth.password_validation import validate_password

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = UserAccount
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'email': {
                'validators': [UniqueValidator(queryset=UserAccount.objects.only('email'), message='Email address must be unique.')]
            }
        }

    def validate(self, data):
        """
        Validate that the 'password' and 're_password' fields match.
        """
        password = data.get('password')
        re_password = data.get('re_password')

        if password and re_password and password != re_password:
            raise serializers.ValidationError("Passwords do not match.")

        validate_password(password)  # Validate other password rules

        return data