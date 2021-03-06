from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.users.api.serializers import MineSerializer
from apps.users.models import Mine


class MineListCreateAPIView(ListCreateAPIView):

    serializer_class = MineSerializer

    def get_queryset(self):
        return Mine.objects.filter(user=self.request.user)


class MineRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    serializer_class = MineSerializer

    def get_queryset(self):
        return Mine.objects.filter(user=self.request.user)
