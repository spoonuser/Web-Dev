"""
URL configuration for shopback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, CategoryDetail, ProductsByCategory

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetail.as_view(), name='product-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetail.as_view(), name='category-detail'),
    path('categories/<int:id>/products/', ProductsByCategory.as_view(), name='products-by-category'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
