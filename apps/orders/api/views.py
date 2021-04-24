from datetime import datetime, timedelta

from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.orders.models import Order
from apps.auction.models import Auction


@api_view(['GET'])
def seller_order_accept(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({"message": "سفارش یافت نشد"}, status=404)

    if order.product.user_id != request.user.id:
        return Response({"message": "شما دسترسی ندارید"}, status=401)

    order.state = Order.STATE_SELLER
    now = datetime.now()

    with transaction.atomic():
        order.save()
        Auction.objects.create(
            start_date=now,
            finish_date=now + timedelta(days=1),
            order=order,
            state=Auction.STATE_STARTED
        )

    return Response({"message": "سفارش با موفقیت تایید شد"}, status=200)


@api_view(['GET'])
def seller_order_reject(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({"message": "سفارش یافت نشد"}, status=404)

    if order.product.user_id != request.user.id:
        return Response({"message": "شما دسترسی ندارید"}, status=401)

    order.is_rejected = True
    order.reject_reason = "سفارش توسط فروشنده لغو شد."
    order.save()

    return Response({"message": "سفارش با موفقیت لغو شد"}, status=200)
