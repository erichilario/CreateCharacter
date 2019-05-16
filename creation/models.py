from django.db import models


class Account(models.Model):
	account_name = 		models.CharField(max_length=100)
	account_password = 	models.CharField(max_length=100)
	account_email = 	models.CharField(max_length=100,blank=True, verbose_name='e-mail')

	def __str__(self):
		return self.account_name

class Race(models.Model):
	race_name = 		models.CharField(max_length=20)
	race_story = 		models.TextField(max_length=500, blank=True)

	def __str__(self):
		return self.race_name

class Job(models.Model):
	job_name = 			models.CharField(max_length=20)
	job_story = 		models.TextField(max_length=500, blank=True)
	race = 				models.ManyToManyField(Race)

	def __str__(self):
		return self.job_name

class Character(models.Model):
	character_name = 	models.CharField(max_length=12) #need a function that pulls "unused" names from a dictionary.txt
	character_date =	models.DateTimeField(blank=True,null=True)
	account = 			models.ForeignKey(Account)
	race =				models.ForeignKey(Race)
	job = 				models.ForeignKey(Job)

	def __str__(self):
		return self.character_name #must be unique