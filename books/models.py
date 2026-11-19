from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    is_available = models.BooleanField(default=True)
    genre = models.CharField(max_length=50, default="Muu")

    def __str__(self):
        return f"{self.title} ({self.author})"