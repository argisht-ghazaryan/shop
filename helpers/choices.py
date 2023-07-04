from django.db import models


class MoneyTypeChoices(models.TextChoices):
    AMD = 'amd', 'AMD'
    USD = 'usd', 'USD'
    RUB = 'rub', 'RUB'
    YUAN = 'yuan', 'YUAN'


class SizeTypeChoices(models.TextChoices):
    S = 'S', 'S'
    M = 'M', 'M'
    L = 'L', 'L'
    XL = 'XL', 'XL'
    XXL = 'XXL', 'XXL'
    BIG = 'BIG', 'big'
    SMALL = 'SMOL', 'small'


class CategoriesTypeChoices(models.TextChoices):
    mobile_phones = 'MOBILE PHONES', 'Mobile Phones'
    computers = 'COMPUTERS', 'Computers'
    electronics = 'ELECTRONICS', 'Electronics'
    home_appliances = 'HOME_APPLIANCES', 'Home Appliances'
    security = 'SECURITY', 'Security'
    automobiles = 'AUTOMOBILES', 'Automobiles'
    furniture = 'FURNITURE', 'Furniture'
    clothing = 'CLOTHING', 'Clothing'
    shoes = 'SHOES', 'Shoes'
    accessories = 'ACCESSORIES', 'Accessories'
    sport = 'SPORT', 'Sport'
    food = 'FOOD', 'Food'
