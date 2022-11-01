from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer

# class ProductViewSet(viewsets.ModelViewSet):
#     """
#     get--> List --> Queryset
#     get--> retrieve --> product instance Detail View
#     post--> Create New Instance
#     put--> Update
#     patch--> Partial Update
#     destroy-->Delete
    
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field  = 'pk'
    
class ProductGenericViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
        """
        get--> List --> Queryset
        get--> retrieve --> product instance Detail View
        
        """
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        lookup_field  = 'pk'
        
# product_list_view      = ProductGenericViewSet.as_view({'get': 'list'})
# product_retrieve_view  = ProductGenericViewSet.as_view({'get': 'retrieve'})