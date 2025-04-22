from django.db import models

class Movie(models.Model) :
    title=models.CharField(max_length=200)
    director=models.CharField(max_length=200)
    rating=models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"{self.title} ({self.rating}/10)"