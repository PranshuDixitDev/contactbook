from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    emai_adress = models.EmailField(max_length=254, unique = True)
    phone_number = models.CharField(
        max_length=13, blank=True, 
        validators=[RegexValidator(
            r'^(\+\d{1,2}|\d{1,2})\s?\d{3}\)?[\d\- ]{0,10}$')])
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateField(auto_now = True)
    
    
    def __str__(self):
        return self.first_name