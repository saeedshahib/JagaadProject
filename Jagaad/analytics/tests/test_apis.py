from decimal import Decimal

from django.test import TestCase
from django.db.models import Sum

from analytics import models as analytics_models


class IntegrationTest(TestCase):

    def create_messages(self):
        payload = {
            "customer_id": 1,
            "type": "A",
            "amount": "0.012"
        }
        for i in range(5):
            self.client.post('/analytics/create-message/', data=payload, content_type='application/json')
        payload = {
            "customer_id": 2,
            "type": "A",
            "amount": "0.015"
        }
        for i in range(5):
            self.client.post('/analytics/create-message/', data=payload, content_type='application/json')
        payload = {
            "customer_id": 1,
            "type": "B",
            "amount": "0.017"
        }
        for i in range(5):
            self.client.post('/analytics/create-message/', data=payload, content_type='application/json')
        payload = {
            "customer_id": 2,
            "type": "B",
            "amount": "0.034"
        }
        for i in range(5):
            self.client.post('/analytics/create-message/', data=payload, content_type='application/json')

    def test_create_message_api(self):
        self.create_messages()

        self.assertEqual(analytics_models.Message.objects.count(), 20)
        self.assertEqual(analytics_models.Message.objects.filter(type='A').aggregate(sum_amount=Sum('amount'))
                         .get('sum_amount'), Decimal('0.135'))
        self.assertEqual(analytics_models.Message.objects.filter(type='B').aggregate(sum_amount=Sum('amount'))
                         .get('sum_amount'), Decimal('0.255'))
        self.assertEqual(analytics_models.Message.objects.filter(customer_id=1).aggregate(sum_amount=Sum('amount'))
                         .get('sum_amount'), Decimal('0.145'))
        self.assertEqual(analytics_models.Message.objects.filter(customer_id=2).aggregate(sum_amount=Sum('amount'))
                         .get('sum_amount'), Decimal('0.245'))

    def test_retrieve_stats_api(self):
        self.create_messages()

        response = self.client.get('/analytics/retrieve-stats/', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(Decimal(str(data[0]['total_amount'])), Decimal("0.06"))  # customer: 1, type: A
        self.assertEqual(Decimal(str(data[1]['total_amount'])), Decimal("0.085"))  # customer: 1, type: B
        self.assertEqual(Decimal(str(data[2]['total_amount'])), Decimal("0.075"))  # customer: 2, type: A
        self.assertEqual(Decimal(str(data[3]['total_amount'])), Decimal("0.17"))  # customer: 2, type: B

        self.create_messages()

        response = self.client.get('/analytics/retrieve-stats/', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(Decimal(str(data[0]['total_amount'])), Decimal("0.12"))  # customer: 1, type: A
        self.assertEqual(Decimal(str(data[1]['total_amount'])), Decimal("0.17"))  # customer: 1, type: B
        self.assertEqual(Decimal(str(data[2]['total_amount'])), Decimal("0.15"))  # customer: 2, type: A
        self.assertEqual(Decimal(str(data[3]['total_amount'])), Decimal("0.34"))  # customer: 2, type: B

