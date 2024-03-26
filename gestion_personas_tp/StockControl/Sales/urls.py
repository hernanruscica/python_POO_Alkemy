from django.urls import path, include  
from . import views
urlpatterns = [
    path('', views.root, name="root") ,
    path('products/', views.products, name="products"),  
    path('products/newform/', views.new_product_form, name="new_product_form"),      
    path('products/create_product', views.create_product, name = "create_product"),
    path('suppliers/', views.suppliers, name="supliers"),
    path('suppliers/newform/', views.new_supplier_form, name = "new_supplier_form"),
    path('suppliers/create_supplier', views.create_supplier, name = "create_supplier"),
    path('test/', views.test, name="test")
]