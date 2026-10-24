from django.db import models
from accounts.models.user import User
from hamdard.storage_backends import PublicMediaStorage

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice = models.FileField(upload_to='invoice', storage=PublicMediaStorage, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.user.email if self.user else None