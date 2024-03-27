from django.contrib import admin
from .models import User, Category, Listing, Bid, Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Comment)

class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Listing,ListingAdmin)