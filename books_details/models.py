from django.db import models

# Create your models here.
class books_details(models.Model):
    title = models.CharField(max_length=200)
    auther = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=255)
    no_of_pages = models.IntegerField()

    def __str__(self):
        return self.title   
