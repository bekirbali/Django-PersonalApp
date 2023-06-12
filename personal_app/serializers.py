from rest_framework import serializers

from .models import Department, Personnel

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'

