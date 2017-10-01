from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products')
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media/products',blank=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()

    def __str__(self):
        return self.name