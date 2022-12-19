from django.contrib.auth import get_user_model
# from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
# from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",            
            "email",
        ]
    

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation

# class CreateUserSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ["id", "username", "email", "first_name", "last_name", "password"]