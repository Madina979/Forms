from django.db import models


class Book(models.Model):
    foto = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    is_read = models.BooleanField(default=False)
    date_read = models.DateField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title