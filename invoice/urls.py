from django.urls import path
from invoice.views.invoice import *


urlpatterns = [
    path('get-invoices', GetInvoiceListAPIView.as_view(), name='get-invoices'),   
    path('create-invoices', InvoiceCreateAPIView.as_view(), name='create-invoices'), 
]
