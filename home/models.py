from django.db import models

# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=100)
    def __str__(self):
        s = str(self.categoryname)
        return s

class Clothes(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    amount = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    categoryname = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        s = str(self.name)
        return s
