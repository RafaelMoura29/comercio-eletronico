from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='index'),
    path('product/<int:pk>', views.productPage, name='product'),
    path('purchase', views.purchasePage, name='purchase'),
    path('cart', views.cartPage, name='cart'),
    path('clientInformations', views.clientInformationsPage, name='clientInformations'),
    path('cadastroProduto', views.cadastroProduto, name='cadastroProduto'),
    path('registerProduct', views.registerProduct, name='registerProduct'),
    path('addToCart/<int:productPk>', views.addToCart, name='addToCart'),
]
