from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=100)
    roll= models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.name

