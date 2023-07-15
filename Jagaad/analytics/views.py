import datetime
from datetime import date

from django.db.models import Count, Sum
from rest_framework import generics, status
from rest_framework.response import Response

from . import serializers as analytics_serializers
from . import models as analytics_models
# Create your views here.


class MessageCreateView(generics.CreateAPIView):
    serializer_class = analytics_serializers.MessageSerializer


class MessageStatsView(generics.RetrieveAPIView):
    serializer_class = analytics_serializers.MessageSerializer

    def get(self, request, *args, **kwargs):
        # Correct date format:  'YYYY-MM-DD', None if you don't want a date interval
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        # Convert the date strings to date objects
        try:
            start_date = date.fromisoformat(start_date) if start_date is not None else datetime.datetime(
                1, 1, 1, tzinfo=datetime.timezone.utc)
        except ValueError:
            return Response({'error': 'Invalid start date format'}, status=400)

        try:
            end_date = date.fromisoformat(end_date) if end_date is not None else datetime.datetime.now(
                tz=datetime.timezone.utc)
        except ValueError:
            return Response({'error': 'Invalid end date format'}, status=400)

        stats = analytics_models.Message.objects\
            .filter(created__gte=start_date, created__lte=end_date)\
            .values('customer_id', 'type')\
            .annotate(count=Count('id'), total_amount=Sum('amount'))

        return Response(stats, status=status.HTTP_200_OK)
