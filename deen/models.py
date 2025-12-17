from django.db import models

# Create your models here.
class Surah(models.Model):
    name = models.CharField(max_length=200)
    description_arabic = models.TextField()

    def __str__(self):
        return self.name


class Dua(models.Model):
    name = models.CharField(max_length=200)
    description_arabic = models.TextField()

    def __str__(self):
        return self.name
    

