from django.db import models


class Promotion(models.Model):
    description = models.TextField()
    discount = models.FloatField()


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey("Collection", on_delete=models.DO_NOTHING)
    promotions = models.ManyToManyField("Promotion")


class Customer(models.Model):
    MEMBERSHIP_CHOICES = [('B', 'bronze'),
                          ('S', 'silver'),
                          ('G', 'gold')]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default='B')


class Orders(models.Model):
    PAYMENT_CHOICES = [('P', 'pending'),
                       ('C', 'complete'),
                       ('F', 'failed')]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default='P')
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)


class Collection(models.Model):
    title = models.CharField(max_length=255)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
# Create your models here.
