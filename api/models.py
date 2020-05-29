from django.db import models


class Category(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=300)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name="Amount",default=None, max_digits=20, decimal_places=2)
    qty =  models.TextField(max_length=300)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.TextField(max_length=255)
    item = models.ForeignKey(Item, verbose_name="Items", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=300)
    location = models.TextField(max_length=300)
    menu = models.ForeignKey(Menu, verbose_name="Menu", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
