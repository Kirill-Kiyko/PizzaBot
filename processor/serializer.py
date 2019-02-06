from rest_framework import serializers
from .models import Pizza

class ProductsTblSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('user_id', 'size', 'payment_type')