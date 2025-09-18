from django import path 
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # Главная страница
    path('catalog/', views.CatalogView.as_view(), name='catalog_all'), # Каталог
    path('catalog/<slug:category_slug>/', views.CatalogView.as_view(), name='catalog'), # Каталог по категории
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'), # Детали продукта
]
