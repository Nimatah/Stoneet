from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.auction.models import Auction


@api_view(['GET'])
def get_auction(request, pk):
    try:
        auction = Auction.objects.get(pk=pk)
    except Auction.DoesNotExist:
        return Response({'message': 'مناقصه پیدا نشد'}, status=404)

    if not request.user.is_authenticated:
        return Response({'message': 'شما دسترسی ندارید'}, status=403)

    if not (request.user.is_logistic or request.user.is_admin or request.user.is_superuser):
        return Response({'message': 'شما دسترسی ندارید'}, status=401)

    lowest_bid = auction.bids.get_lowest_price()
    if lowest_bid:
        price = lowest_bid.price
    else:
        price = '-'

    return Response({
        'id': auction.id,
        'start_date': auction.get_persian_start_date().strftime('%Y-%m-%d'),
        'finish_date': auction.get_persian_finish_date().strftime('%Y-%m-%d'),
        'order': {
            'id': auction.order.id,
            'weight': f'{auction.order.weight} {auction.order.product.get_price().get_weight_unit_display()}',
            'category': auction.order.product.category.title,
            'delivery_type': auction.order.product.get_delivery_type(),
            'monthly_load': f'{auction.order.monthly_load} ماه',
            'monthly_load_weight': f'{auction.order.get_monthly_weight()} {auction.order.product.get_price().get_weight_unit_display()}',
        },
        'source': {
            'province': auction.order.product.mine.region.parent.title,
            'city': auction.order.product.mine.region.title,
            'address': auction.order.product.mine.address,
        },
        'destination': {
            'province': auction.order.destination.region.parent.title,
            'city': auction.order.destination.region.title,
            'address': auction.order.destination.address,
        },
        'min_bid': price,
        'my_bid': getattr(auction.bids.filter(user=request.user).order_by('price').first(), 'price', '-')
    })


@api_view(['POST'])
def create_bid(request, pk):
    try:
        auction = Auction.objects.get(pk=pk)
    except Auction.DoesNotExist:
        return Response({'message': 'مناقصه پیدا نشد'}, status=404)

    if not request.user.is_authenticated:
        return Response({'message': 'شما دسترسی ندارید'}, status=403)

    if not (request.user.is_logistic or request.user.is_admin or request.user.is_superuser):
        return Response({'message': 'شما دسترسی ندارید'}, status=401)

    if auction.bids.filter(user=request.user).exists() and \
            auction.bids.filter().order_by('price').first() == request.user:
        return Response({'message': 'شما قبلا در این مناقصه شرکت کرده اید'}, status=400)

    price = request.data.get('price')
    try:
        price = int(price)
        if price < 100000:
            return Response({'message': 'قیمت وارد شده اشتباه است'}, status=400)
    except:
        return Response({'message': 'قیمت وارد شده اشتباه است'}, status=400)

    auction.bids.create(user=request.user, price=price)

    return Response({'message': 'درخواست شما با موفقیت ثبت شد'})


@api_view(['GET'])
def get_auction_admin(request, pk):
    try:
        auction = Auction.objects.get(pk=pk)
    except Auction.DoesNotExist:
        return Response({'message': 'مناقصه پیدا نشد'}, status=404)

    if not request.user.is_authenticated:
        return Response({'message': 'شما دسترسی ندارید'}, status=403)

    if not (request.user.is_admin or request.user.is_superuser):
        return Response({'message': 'شما دسترسی ندارید'}, status=401)

    lowest_bid = auction.bids.get_lowest_price()
    if lowest_bid:
        price = lowest_bid.price
    else:
        price = '-'

    return Response({
        'id': auction.id,
        'start_date': auction.get_persian_start_date().strftime('%Y-%m-%d %H:%m:%S'),
        'finish_date': auction.get_persian_finish_date().strftime('%Y-%m-%d %H:%m:%S'),
        'finish_timestamp': auction.finish_date,
        'order': {
            'id': auction.order.id,
            'weight': auction.order.weight,
            'category': auction.order.product.category.title,
            'delivery_type': auction.order.product.get_delivery_type(),
            'monthly_load': auction.order.monthly_load,
            'monthly_load_weight': auction.order.get_monthly_weight(),
        },
        'source': {
            'province': auction.order.product.mine.region.parent.title,
            'city': auction.order.product.mine.region.title,
            'address': auction.order.product.mine.address,
        },
        'destination': {
            'province': auction.order.destination.region.parent.title,
            'city': auction.order.destination.region.title,
            'address': auction.order.destination.address,
        },
        'min_bid': price,
    })


@api_view(['GET'])
def reactivate_auction(request, pk):
    try:
        auction = Auction.objects.get(pk=pk)
    except Auction.DoesNotExist:
        return Response({'message': 'مناقصه پیدا نشد'}, status=404)

    if not request.user.is_authenticated:
        return Response({'message': 'شما دسترسی ندارید'}, status=403)

    if not (request.user.is_admin or request.user.is_superuser):
        return Response({'message': 'شما دسترسی ندارید'}, status=401)

    auction.set_state_started()

    return Response({}, status=200)
