from rest_framework.generics import ListAPIView

from apps.products.api.serializers import ProductSerializer
from apps.products.models import Product


class ListProductAPIView(ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
