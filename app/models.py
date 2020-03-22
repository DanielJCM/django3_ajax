from django.db import models
from app.constantes import * 

class Book(models.Model):

    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.CharField(choices=book_types,max_length=120)

    def __str__(self):
        return self.title
