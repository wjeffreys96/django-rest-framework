from rest_framework import mixins, viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  # default


class ProductGenericViewset(
        mixins.ListModelMixin, 
        mixins.RetrieveModelMixin, 
        viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  # default
