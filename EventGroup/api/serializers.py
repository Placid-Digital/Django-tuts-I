import rest_framework
from django.forms import Field
from rest_framework import serializers
from django.contrib.auth.models import User



from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
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
#         user = User.objects.create_user(validated_data['username'], validated_data['email'],
#                                         validated_data['password'])
#
#         return user
