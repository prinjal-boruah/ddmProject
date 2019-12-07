from django.db import models

class Schools(models.Model):
	school_name = models.CharField(max_length = 100)
	established = models.IntegerField()

	def __str__(self):
		return self.school_name

class Colleges(models.Model):
	college_name = models.CharField(max_length = 100)
	established = models.IntegerField()

	def __str__(self):
		return self.college_name