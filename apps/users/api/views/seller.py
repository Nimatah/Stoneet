from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.api.serializers import SellerAddProductPart1ValidationSerializer


class SellerAddProductPart1ValidationAPIView(APIView):

    serializer_class = SellerAddProductPart1ValidationSerializer

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=False):
            return Response(status=status.HTTP_200_OK)
        response = {}
        for k, v in serializer.errors.items():
            response[serializer.fields[f'{k}'].label] = v

        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
