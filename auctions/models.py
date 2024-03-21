from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"{self.username} {self.email} {self.password}"


class Category(models.Model):
    title = models.CharField(max_length = 20)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "categories"

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_listings")
    categories = models.ManyToManyField(Category, related_name="categories_listings")
    title = models.CharField(max_length = 50)
    description = models.TextField(blank=True)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.user} {self.starting_bid} {self.created_at}"

    
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    Listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_bids")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Listing} {self.user} {self.amount} {self.created_at}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    Listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comments")
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.Listing} {self.text} {self.created_at}"