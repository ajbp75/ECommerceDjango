from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_imagem = models.CharField(max_length=500, default="https://2.bp.blogspot.com/-D1dooVSafi4/V9vwv4fEYYI/AAAAAAABFQU/GgOCoa6c6OsnRyLFZJY-m9Dax59ZZAPOwCEw/s640/burrito.jpg")
