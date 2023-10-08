from django.db import models
from django.contrib.auth.models import User  # Use Django's built-in User model for authentication

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status_choices = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Establish a foreign key relationship with User model

    def __str__(self):
        return self.title
