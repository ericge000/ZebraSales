from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    # Retitles categories so that it is spelled correctly
    class Meta:
        
        # Sorts categories alphabetically
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    # Retitles the objects so that they are called their 
    # names instead of Category object (1), etc.
    def __str__(self):
        return self.name
    
# Sets up basic descriptions for Item objects
class Item(models.Model):
    # CASCADE deletes all items if a category is deleted
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    # Creates a folder for image uploads
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    # CASCADE deletes all items if a user is deleted
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name