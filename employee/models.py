from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name}'