from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.resto.views import RestoDetailView, RestoViewSet, RestoListView, MenuViewSet, MenuListView, FoodViewSet, \
    FoodDetailView, MenuDetailView

#
router = DefaultRouter()
router.register('resto', RestoViewSet)
router.register('menu', MenuViewSet)
router.register('food', FoodViewSet)
urlpatterns = [
    path('resto-list/<int:pk>/', RestoDetailView.as_view()),
    path('menu/<int:pk>/', MenuDetailView.as_view()),
    path('food/<int:pk>/', FoodDetailView.as_view()),
    path('', include(router.urls)),
]
urlpatterns.extend(router.urls)
