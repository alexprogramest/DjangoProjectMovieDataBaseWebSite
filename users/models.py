from django.db import models


# Create your models here.
class MovieDBUser(models.Model):
    nick_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=30)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    directory_name = models.CharField(max_length=20)
    # favourite_movies = models.ManyToManyField(TheMovie)

    def __str__(self):
        return self.nick_name
