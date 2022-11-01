from django.urls import path
from . import views 

#/api/
urlpatterns =[
    path("list/", views.product_list_create_view, name="product-list"),                 #views.product_alt_view
    path("<int:pk>/", views.ProductDetailAPIView.as_view(), name="product-detail"),  #views.product_alt_view
    path("<int:pk>/update/", views.product_update_view, name="product-edit"),
    path("<int:pk>/delete/", views.product_delete_view),
    path("", views.product_mixins_view),   
    
]