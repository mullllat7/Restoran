from rest_framework import serializers
from .models import Order
from ..resto.models import Resto


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user_id'] = request.user
        order = Order.objects.create(**validated_data)
        return order

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('id')
        representation['user'] = f'{instance.user}'
        return representation
