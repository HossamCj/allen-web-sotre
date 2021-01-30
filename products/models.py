from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=124)
    description = models.TextField(max_length=500, blank=True, null=True)
    brand = models.CharField(max_length=124)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product_details', args=(self.id,))

    def __str__(self):
        return self.title
