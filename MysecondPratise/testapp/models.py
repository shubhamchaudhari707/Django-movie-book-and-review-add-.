from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Myuser(AbstractUser):
    mobile = models.CharField(max_length=12)
    wallet_amount = models.FloatField(default=100)

    class Meta:
        db_table = 'myuser'

    def __str__(self):
        return self.username


class MyCategory(models.Model):
    category = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.category


class MyLanguges(models.Model):
    language = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.language


class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='movie/images')
    price = models.FloatField(default=0)
    category = models.ForeignKey(MyCategory, on_delete=models.CASCADE)
    language = models.ForeignKey(MyLanguges, on_delete=models.CASCADE, default='')
    cast = models.CharField(max_length=100)
    year_of_production = models.DateField()
    slug = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.title

class BookMovie(models.Model):
    user = models.ForeignKey(Myuser, on_delete=models.CASCADE, default='')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(default=timezone.now)
    booking_date = models.DateField(default=timezone.now)


    def __str__(self):
        return self.user.username + ' - ' + self.movie.title

class ReviewMovie(models.Model):
    user = models.ForeignKey(Myuser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    reviews = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.rating

