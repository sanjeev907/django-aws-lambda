import random
import string
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    
    
    mobile_regex = RegexValidator(regex=r'^[6-9]\d{9}$',message="Enter valid 10 digit mobile number")
    
    username = None
    
    
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10, null=True, blank=True, unique=True, validators=[mobile_regex])
    otp = models.CharField(max_length=4, null=True, blank=True, unique=True)
    referral_code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    referral_by = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def generate_referral_code(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    
    def save(self, *args, **kwargs):
        
        if not self.referral_code:
            code = self.generate_referral_code()

            while User.objects.filter(referral_code=code).exists():
                code = self.generate_referral_code()

            self.referral_code = code

        super().save(*args, **kwargs)

    def __str__(self):
        return self.email