from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

# class UserSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'phone')


# Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password', 'phone')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         users = User.objects.create_user(validated_data['username'], validated_data['email'],
#                                         validated_data['password'])
#
#         return users
