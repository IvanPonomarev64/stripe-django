from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name