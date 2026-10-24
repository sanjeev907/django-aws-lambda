from rest_framework.serializers import ModelSerializer
from invoice.models.invoice import Invoice
from rest_framework import serializers
from accounts.models.user import *


class InvoiceViewSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        
        
class InvoiceCreateSerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    invoice = serializers.FileField(required=True)
    
    class Meta:
        model = Invoice
        fields = ('user', 'invoice')