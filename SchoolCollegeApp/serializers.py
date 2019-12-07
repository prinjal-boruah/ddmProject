from rest_framework import serializers
from . models import *

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = '__all__'

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colleges
        fields = '__all__'