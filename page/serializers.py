from rest_framework import serializers
from .models import Bhav

class BhavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bhav
        fields = '__all__'