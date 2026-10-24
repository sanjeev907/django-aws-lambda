from rest_framework.generics import ListAPIView, CreateAPIView
from accounts.models.user import *
from invoice.models.invoice import Invoice
from invoice.serializers.invoice import *


class GetInvoiceListAPIView(ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceViewSerializer
    
    
class InvoiceCreateAPIView(CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceCreateSerializer