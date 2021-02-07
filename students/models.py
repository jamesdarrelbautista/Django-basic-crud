from django.db import models
from django.forms import ModelForm

# Create your models here.

class Students(models.Model):
    f_name = models.CharField(max_length = 55)
    l_name = models.CharField(max_length =55)
    email = models.CharField(max_length=111)
    
class Meta:
    db_table = "students"