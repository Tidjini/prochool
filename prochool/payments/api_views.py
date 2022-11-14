from rest_framework import viewsets

from .serializers import PaymentSerializer
from .models import Payment


class PaymentApiViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
