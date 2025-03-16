from django.db import models

# Create your models here.

class Employee(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  email=models.EmailField(unique=True, max_length=254)
  contact=models.IntegerField()
  password=models.CharField(max_length=12)

  def __str__(self):
      return f'{self.id}'