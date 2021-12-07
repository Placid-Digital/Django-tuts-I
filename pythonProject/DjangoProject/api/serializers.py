from rest_framework import serializers
from api.models import Person, Species



class PersonSerializer(serializers.ModelSerializer):
   class Meta:
       model = Person
       fields = ('first_name', 'Email', 'Password')


class SpeciesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Species
       fields = ('classification', 'language')