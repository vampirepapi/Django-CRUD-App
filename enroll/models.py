from django.db import models

# Create your models here.
class User(models.Model):
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	std = models.CharField(max_length = 20, default="Not Assigned")

	# def __str__(self):
	# 	return self.name

