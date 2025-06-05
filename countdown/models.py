from django.db import models
from django.urls import reverse

# Create your models here.
class Birthday(models.Model):
	name = models.CharField(max_length=255)
	date = models.DateTimeField()
	month = models.IntegerField()
	day = models.IntegerField()

	def __str__(self):
		return f'{self.name}'

	def get_absolute_url(self):
		return reverse('countdown:countdown_detail', args=[self.pk])

	class Meta:
		ordering = ['month', 'day']
