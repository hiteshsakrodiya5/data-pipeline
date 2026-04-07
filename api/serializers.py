from rest_framework import serializers
from .models import DataJob

class DataJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataJob
        fields = '__all__'