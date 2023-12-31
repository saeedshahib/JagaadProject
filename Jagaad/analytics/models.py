import uuid as uuid

from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Message(BaseModel):
    class MessageType(models.TextChoices):
        A = "A"
        B = "B"
        C = "C"
        D = "D"
    customer_id = models.IntegerField()
    type = models.CharField(max_length=255, default="", choices=MessageType.choices)
    amount = models.DecimalField(max_digits=8, decimal_places=3)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
