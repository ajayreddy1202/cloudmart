from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id', 'user_id', 'email', 'notification_type',
            'subject', 'message', 'status', 'created_at', 'sent_at'
        ]


class SendNotificationSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    email = serializers.EmailField()
    notification_type = serializers.ChoiceField(choices=[
        'order_placed', 'order_confirmed',
        'order_shipped', 'order_delivered', 'order_cancelled'
    ])
    order_id = serializers.IntegerField()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)