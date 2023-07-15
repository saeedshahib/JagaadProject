from rest_framework import serializers

from . import models as analytics_models


class MessageSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(required=False)

    class Meta:
        model = analytics_models.Message
        fields = ["customer_id", "type", "amount", "uuid"]

