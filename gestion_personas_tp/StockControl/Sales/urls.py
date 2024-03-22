from django.urls import path, include  
from . import views
urlpatterns = [
    path('', views.root, name="root") ,
    path('products/', views.products, name="products"),    
    path('suppliers/', views.suppliers, name="supliers")
]