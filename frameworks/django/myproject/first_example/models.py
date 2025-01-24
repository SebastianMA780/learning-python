from django.db import models

# Create your models here.
class Car(models.Model):
		name = models.CharField(max_length=100)
		description = models.TextField(max_length=255)
		year = models.IntegerField(max_length=4, null=True)

		def __str__(self):
				return self.name