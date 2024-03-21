from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    title = models.CharField(max_length = 20)

class Auction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_auctions")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category_auctions")
    title = models.CharField(max_length = 50)
    description = models.TextField(blank=True)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="user_bids")
    auction = models.ForeignKey(Auction, on_delete=models.SET_NULL, related_name="auction_bids")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="user_comments")
    auction = models.ForeignKey(Auction, on_delete=models.SET_NULL, related_name="auction_comments")
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)