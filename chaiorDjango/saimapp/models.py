from django.db import models
from django.utils import timezone
# Create your models here.
class ChaiVarity(models.Model):
   CHAI_TYPR_CHOICE =[
      ('ML','MASALA')
      ('GR','GINJAR')
      ('KI','KIWI')
     ]
   name = models.CharField(max_length=100)
   image = models.models.ImageField(upload_to='chais/')
   date_added = models.DateTimeField(default=timezone.now)
