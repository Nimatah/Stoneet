from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.users.api.serializers import AddressSerializer
from apps.users.models import Address


class AddressListCreateAPIView(ListCreateAPIView):

    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)


class AddressRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
