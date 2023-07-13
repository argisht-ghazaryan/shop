from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from helpers.upload_files import upload_product_image
from helpers.choices import MoneyTypeChoices, SizeTypeChoices, CategoriesTypeChoices


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255, null=True, blank=True)
    count = models.DecimalField(max_digits=10, decimal_places=0)
    amount = models.DecimalField(max_digits=10, decimal_places=1)
    currency = models.CharField(max_length=25, choices=MoneyTypeChoices.choices)
    description = models.TextField(null=True, blank=True)
    size = models.CharField(max_length=50, choices=SizeTypeChoices.choices, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    photo = models.ImageField(upload_to=upload_product_image)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey('Categories', on_delete=models.CASCADE)
    # character = models.ForeignKey('Character', on_delete=models.CASCADE, verbose_name='Characteristics')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ditail', kwargs={'pk': self.pk})


class Categories(models.Model):
    name = models.CharField(max_length=255, choices=CategoriesTypeChoices.choices)

    def __str__(self):
        return self.name


# class Character(models.Model):
#     other = models.CharField(max_length=155, null=True, blank=True)
#     origin = models.CharField(max_length=200)
#     certification = models.CharField(max_length=155, null=True, blank=True)
#     brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True, blank=True)
#
#     def __str__(self):
#         return f'{self.brand} {self.origin}'


# class Brand(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
