import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from app.account.permissions import IsActivePermission
from app.resto.models import Resto, Menu, Food


class RestoNames:

    def get_restos(self):
        return Resto.objects.all()

    def get_names(self):
        return Resto.resto_name.filter(draft=True)


from app.resto.serializers import RestoSerializer, RestoDetailSerializer, MenuSerializer, FoodSerializer, \
    FoodDetailSerializer, MenuDetailSerializer


class RestoListView(generics.ListAPIView, RestoNames):
    queryset = Resto.objects.all()
    serializer_class = RestoSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsActivePermission]

    def get_serializer_context(self):
        return {'request':self.request}


class RestoDetailView(generics.ListAPIView, RestoNames):
    queryset = Resto.objects.all()
    serializer_class = RestoDetailSerializer
    permission_classes = [IsActivePermission]


class RestoViewSet(viewsets.ModelViewSet):
    queryset = Resto.objects.all()
    serializer_class = RestoSerializer
    permission_classes = [IsAuthenticated, ]

    @action(detail=False, methods=['get'])
    def ordered(self, request, pk=None):
        orders = Order.objects.filter(user=request.user)


# --------------------------------Menu------------------------------------


# --------------------------------Menu------------------------------------

class MenuListView(generics.ListAPIView, RestoNames):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsActivePermission]

    def get_serializer_context(self):
        return {'request':self.request}


class MenuDetailView(generics.ListAPIView, RestoNames):
    queryset = Menu.objects.all()
    serializer_class = MenuDetailSerializer
    permission_classes = [IsActivePermission]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, ]


# --------------------------------Menu------------------------------------
# --------------------------------Menu------------------------------------


class FoodListView(generics.ListAPIView, RestoNames):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsActivePermission]

    def get_serializer_context(self):
        return {'request': self.request}


class FoodDetailView(generics.ListAPIView, RestoNames):
    queryset = Food.objects.all()
    serializer_class = FoodDetailSerializer
    permission_classes = [IsActivePermission]


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated, ]

