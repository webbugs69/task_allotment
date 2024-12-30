from django.db import models

# Create your models here.

class details(models.Model):
    username = models.CharField(max_length=100 , unique= True)
    email = models.EmailField(max_length= 254 , default= 'null ' ,unique= True )
    password = models.CharField(max_length= 100)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length= 100 , default = 'default' , blank = True)
    
    def __str__(self):
        return self.username
