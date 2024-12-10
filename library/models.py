from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    availability_status = models.BooleanField(default=True)  # True = Available

    def __str__(self):
        return f"{self.title} - {self.isbn}"

class BorrowRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    class Meta:
        unique_together = ('book', 'start_date', 'end_date')  # Prevent overlapping dates

    def __str__(self):
        return f"{self.user.username} requested {self.book.title} ({self.status})"
