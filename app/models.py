from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class ExampleModel(models.Model):
	alias = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	first_name = models.CharField(max_length=255, null=True)
	last_name = models.CharField(max_length=255, null=True)
	email = models.EmailField(null=True)