from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer, CreateOrderSerializer
from decimal import Decimal


@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        user_id = request.query_params.get('user_id', None)
        if user_id:
            orders = Order.objects.filter(user_id=user_id)
        else:
            orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CreateOrderSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            order = Order.objects.create(
                user_id=data['user_id'],
                shipping_address=data['shipping_address'],
                status='pending'
            )
            total = Decimal('0')
            for item in data['items']:
                order_item = OrderItem.objects.create(
                    order=order,
                    product_id=item['product_id'],
                    product_name=item['product_name'],
                    quantity=item['quantity'],
                    price=Decimal(str(item['price']))
                )
                total += order_item.subtotal
            order.total_amount = total
            order.save()
            return Response(
                OrderSerializer(order).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'message': 'Order not found!'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        new_status = request.data.get('status')
        if new_status not in dict(Order.STATUS_CHOICES):
            return Response({'message': 'Invalid status!'}, status=status.HTTP_400_BAD_REQUEST)
        order.status = new_status
        order.save()
        return Response(OrderSerializer(order).data)

    elif request.method == 'DELETE':
        order.delete()
        return Response({'message': 'Order deleted!'}, status=status.HTTP_204_NO_CONTENT)