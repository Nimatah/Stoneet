from rest_framework.generics import UpdateAPIView

from .serializers import StaticContentSerializer
from ..models import StaticContent


class StaticContentUpdateAPIView(UpdateAPIView):

    serializer_class = StaticContentSerializer
    queryset = StaticContent.objects.all()
    lookup_field = 'pk'
