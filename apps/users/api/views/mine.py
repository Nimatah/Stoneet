from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.api.serializers import MineSerializer
from apps.users.models import Mine


class MineListCreateAPIView(ListCreateAPIView):

    serializer_class = MineSerializer

    def get_queryset(self):
        return Mine.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        response = {}
        for k, v in serializer.errors.items():
            response[serializer.fields[f'{k}'].label] = v
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

class MineRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    serializer_class = MineSerializer

    def get_queryset(self):
        return Mine.objects.filter(user=self.request.user)
