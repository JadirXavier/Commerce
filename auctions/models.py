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
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_listings")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category_listings")
    title = models.CharField(max_length = 50)
    description = models.TextField(blank=True, null=True)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length = 100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.user} {self.starting_bid} {self.created_at}"

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,  related_name="listing_bids")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.listing} {self.user} {self.amount} {self.created_at}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comments")
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.listing} {self.text} {self.created_at}"