from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet



router=DefaultRouter()
router.register(r'products',ProductViewSet,basename='product')

urlpatterns=[
   #path('products/',ProductListView.as_view(),name='product_List'),
   #path('products/<int:pk>',ProductDetailsView.as_view(),name='product_detail'),
    path('',include(router.urls)),
]