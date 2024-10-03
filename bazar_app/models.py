from django.db import models
from django.utils import timezone
# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag (TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(TimeStampModel):
    STATUS_CHOICES = [
        ("active","Active"),
        ("in_active","Inactive"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False)
    video_link = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    published_at = models.DateTimeField(null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    price = models.DecimalField(max_digits= 9999999, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    

class Contact(TimeStampModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length = 200)
    message = models.TextField()

    def __str__(self):
        return self.name


class UserProfile(TimeStampModel):
    user = models.OneToOneField("auth.user", on_delete=models.CASCADE)
    address = models.CharField(max_length =200)
    phone = models.CharField(max_length = 10)

    def __str__(self):
        return self.user.username
    

# Order model
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("shipped", "Shipped"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'


# OrderItem model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.product.title}'