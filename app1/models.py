from django.db import models

# Create your models here.
CHOICES=[("CS","Computer science"),
         ("AMC","Applied Matghematics and Computing"),
         ("ENS","Environment Science"),
         ]
class student(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    regno=models.IntegerField()
    register_date=models.DateField(auto_now=False, auto_now_add=False)
    email=models.EmailField( max_length=254)
    branch=models.CharField(max_length=50,choices=CHOICES,default="Unknown")
    
    def __str__(self):
        return "f{self.fname}"

    

     
 
 