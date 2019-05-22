from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Account(models.Model):
	user 				= models.OneToOneField(User, related_name='profile')
	account_password 	= models.CharField(max_length=100)
	account_email 		= models.CharField(max_length=100,blank=True, verbose_name='e-mail')

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('creation:profile', args=[self.user.username])

class Race(models.Model):
	race_name 			= models.CharField(max_length=20)
	race_story 			= models.TextField(max_length=500, blank=True)

	def __str__(self):
		return self.race_name

class Job(models.Model):
	job_name 			= models.CharField(max_length=20)
	job_story 			= models.TextField(max_length=500, blank=True)
	race 				= models.ManyToManyField(Race)

	def __str__(self):
		return self.job_name

class Color(models.Model):
	color_name 			= models.CharField(max_length=6)

	def __str__(self):
		return self.color_name

class Hair(models.Model):
	hair_name 			= models.CharField(max_length=5)

	def __str__(self):
		return self.hair_name

class Face(models.Model):
	face_name 			= models.CharField(max_length=5)

	def __str__(self):
		return self.face_name

class Sex(models.Model):
	sex_name 			= models.CharField(max_length=6)

	def __str__(self):
		return self.sex_name

class Character(models.Model):
	character_name 		= models.CharField(max_length=12, unique=True) #need a function that pulls "unused" names from a dictionary.txt
	slug 				= models.SlugField(max_length=12, null=True, blank=True, unique=True)
	character_date 		= models.DateTimeField(blank=True,null=True,auto_now_add=True)
	character_update 	= models.DateTimeField(blank=True,null=True,auto_now=True)
	account 			= models.ForeignKey(Account)
	race 				= models.ForeignKey(Race)
	job 				= models.ForeignKey(Job, verbose_name="Class")
	color 				= models.ForeignKey(Color, default="1")
	hair 				= models.ForeignKey(Hair, default="1")
	face 				= models.ForeignKey(Face, default="1")
	sex 				= models.ForeignKey(Sex, default="1")

	class Meta:
		ordering = ['account','character_name']

	def __str__(self):
		return self.character_name
	
	def get_absolute_url(self):
		return "/character/%d/" % self.id #fix later, maybe

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
