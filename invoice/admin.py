from django.contrib import admin
from invoice.models.invoice import *



# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at',)

admin.site.register(Invoice, InvoiceAdmin)