from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.api.serializers import ProductSerializer
from apps.products.models import Product, Category


class ListProductAPIView(ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET', ])
def product_accept(request, pk):
    if not request.user.is_authenticated and not (request.user.is_admin or request.user.is_superuser):
        return Response({'error': 'شما دسترسی ندارید'}, status=401)

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'محصول پیدا نشد'}, status=404)

    product.state = Product.STATE_ACCEPTED
    product.rejection_reason = ''
    product.save()

    return Response('', status=200)


@api_view(['GET', ])
def product_reject(request, pk):
    if not request.user.is_authenticated and not (request.user.is_admin or request.user.is_superuser):
        return Response({'error': 'شما دسترسی ندارید'}, status=401)

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'محصول پیدا نشد'}, status=404)

    product.state = Product.STATE_REJECTED
    product.reject_reason = request.query_params.get('reason')
    product.save()

    return Response('', status=200)
