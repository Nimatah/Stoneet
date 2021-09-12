from datetime import datetime, timedelta

from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from apps.invoices.models import Invoice
from apps.orders.models import Order, OrderMedia
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


@api_view(['POST', ])
def save_order_contract_images(request: Request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({"message": "سفارش یافت نشد"}, status=404)

    if order.buyer_id != request.user.id:
        return Response({"message": "شما دسترسی ندارید"}, status=401)

    data = request.data

    for image in data.values():
        if not image or isinstance(image, str):
            continue
        order.media.create(
            title='signed_contract',
            file=image,
            type=OrderMedia.TYPE_IMAGE
        )
    return Response("", status=200)


@api_view(['POST', ])
def save_order_finance_images(request: Request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({"message": "سفارش یافت نشد"}, status=404)

    if order.buyer_id != request.user.id:
        return Response({"message": "شما دسترسی ندارید"}, status=401)

    data = request.data

    for image in data.values():
        if not image or isinstance(image, str):
            continue
        order.media.create(
            title='finance',
            file=image,
            type=OrderMedia.TYPE_IMAGE
        )
    return Response("", status=200)


@api_view(['DELETE', ])
def remove_order_image(request, pk, image_pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({"message": "سفارش یافت نشد"}, status=404)

    if order.buyer_id != request.user.id:
        return Response({"message": "شما دسترسی ندارید"}, status=401)

    if not OrderMedia.objects.filter(pk=image_pk).exists():
        return Response({"message": "عکس یافت نشد"}, status=404)

    OrderMedia.objects.get(pk=image_pk).delete()

    return Response("", status=200)


@api_view(['GET', ])
def accept_order(request: Request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({"message": "سفارش یافت نشد"}, status=404)

    if order.buyer_id != request.user.id:
        return Response({"message": "شما دسترسی ندارید"}, status=401)

    order.state = Order.STATE_ACCEPTED
    order.save()

    order.invoice_set.update(state=Invoice.STATE_UNPAID)

    return Response(None, status=200)
