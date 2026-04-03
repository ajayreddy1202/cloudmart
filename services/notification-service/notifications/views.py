from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Notification
from .serializers import NotificationSerializer, SendNotificationSerializer


def get_message(notification_type, order_id, total_amount):
    messages = {
        'order_placed': {
            'subject': f'Order #{order_id} Placed Successfully!',
            'message': f'Thank you for shopping at CloudMart! Your order #{order_id} has been placed successfully. Total amount: Rs.{total_amount}. We will confirm your order shortly.'
        },
        'order_confirmed': {
            'subject': f'Order #{order_id} Confirmed!',
            'message': f'Great news! Your order #{order_id} has been confirmed. Total amount: Rs.{total_amount}. We are preparing your items.'
        },
        'order_shipped': {
            'subject': f'Order #{order_id} Shipped!',
            'message': f'Your order #{order_id} is on the way! Total amount: Rs.{total_amount}. You will receive it within 3-5 business days.'
        },
        'order_delivered': {
            'subject': f'Order #{order_id} Delivered!',
            'message': f'Your order #{order_id} has been delivered successfully! Total amount: Rs.{total_amount}. Thank you for shopping with CloudMart!'
        },
        'order_cancelled': {
            'subject': f'Order #{order_id} Cancelled',
            'message': f'Your order #{order_id} has been cancelled. Total amount: Rs.{total_amount}. If you have any questions, please contact support.'
        },
    }
    return messages.get(notification_type, {'subject': 'CloudMart Notification', 'message': ''})


@api_view(['POST'])
def send_notification(request):
    serializer = SendNotificationSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        msg = get_message(
            data['notification_type'],
            data['order_id'],
            data['total_amount']
        )
        notification = Notification.objects.create(
            user_id=data['user_id'],
            email=data['email'],
            notification_type=data['notification_type'],
            subject=msg['subject'],
            message=msg['message'],
            status='sent',
            sent_at=timezone.now()
        )
        return Response({
            'message': 'Notification sent successfully!',
            'notification': NotificationSerializer(notification).data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def notification_list(request):
    user_id = request.query_params.get('user_id', None)
    if user_id:
        notifications = Notification.objects.filter(user_id=user_id)
    else:
        notifications = Notification.objects.all()
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def notification_detail(request, pk):
    try:
        notification = Notification.objects.get(pk=pk)
    except Notification.DoesNotExist:
        return Response({'message': 'Notification not found!'}, status=status.HTTP_404_NOT_FOUND)
    serializer = NotificationSerializer(notification)
    return Response(serializer.data)