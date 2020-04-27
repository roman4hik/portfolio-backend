from rest_framework import serializers

from users.models import User


class RegistrationSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, write_only=True)
    password_2 = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    date_of_birthday = serializers.DateTimeField(required=False)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        password = attrs["password"]
        password_2 = attrs["password_2"]
        if password != password_2:
            raise serializers.ValidationError(
                {"password": "passwords are different"}  # fmt: off
            )
        return attrs

    def validate_email(self, attr):
        if User.objects.filter(email=attr).exists():
            raise serializers.ValidationError("Email already exist")
        return attr

    def validate_username(self, attr):
        if User.objects.filter(username=attr).exists():
            raise serializers.ValidationError("Username already exist")
        return attr

    def save(self, **kwargs):
        data = self.validated_data
        data.pop("password_2")
        User.objects.create_user(**data)
