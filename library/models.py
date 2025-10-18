from django.db import models

# Create your models here.

 

class Research(models.Model):
    titler = models.CharField(max_length=150)
    authorr = models.CharField(max_length=100)

    def __str__(self):
        return self.titler

