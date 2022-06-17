from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from app.order.models import Order
from app.order.serializers import OrderSerializer
from app.resto.models import Resto


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, ]

    # if Order.order_time > :


class OrderView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(
            user=user
        )
        return queryset
