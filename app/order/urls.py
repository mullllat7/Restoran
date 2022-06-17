from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import OrderViewSet

router = DefaultRouter()
router.register('', OrderViewSet)

urlpatterns = [
    path('own_orders/', views.OrderView.as_view()),
]
urlpatterns.extend(router.urls)

