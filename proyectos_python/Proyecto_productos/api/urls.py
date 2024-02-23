# urls.py
from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'Productos', views.ProductosViewSet)
router.register(r'Order', views.OrderViewSet)
router.register(r'OrderItem', views.OrderItemViewSet)
router.register(r'Categoria', views.CategoriaViewSet)
router.register(r'Customer', views.CustomerViewSet)
router.register(r'Operator', views.OperatorViewSet)

urlpatterns = [
    path('', include(router.urls))
]
