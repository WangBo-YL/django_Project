from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('BOOK', 'Book'),
        ('VIDEO', 'Video'),
        ('GAME', 'Game'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default='BOOK')
    is_borrowed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class BorrowRecord(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='borrow_records')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrow_records')
    borrow_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.item.title} borrowed by {self.borrower.username}'

    class Meta:
        ordering = ['-borrow_date']

class Book(Item):
    author = models.CharField(max_length=100)
    publish_date = models.DateField(null=True, blank=True)
    ISBN = models.CharField(max_length=13, unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.title} by {self.author}'

class Video(Item):
    director = models.CharField(max_length=100)
    release_year = models.IntegerField(null=True, blank=True)
    duration_minutes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} directed by {self.director}'

class Game(Item):
    platform = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} on {self.platform}'
