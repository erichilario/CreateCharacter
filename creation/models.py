from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class Account(models.Model):
	user = 				models.OneToOneField(User, related_name='profile')
	#account_name = 		models.CharField(max_length=100)
	account_password = 	models.CharField(max_length=100)
	account_email = 	models.CharField(max_length=100,blank=True, verbose_name='e-mail')

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('creation:profile', args=[self.user.username])

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
	character_name = 	models.CharField(max_length=12, unique=True) #need a function that pulls "unused" names from a dictionary.txt
	character_date =	models.DateTimeField(blank=True,null=True)
	account = 			models.ForeignKey(Account)
	race =				models.ForeignKey(Race)
	job = 				models.ForeignKey(Job)

	def __str__(self):
		return self.character_name #must be unique

# @receiver(post_save, sender=User)
# def create_user(sender, **kwargs):
#     if kwargs.get('created', False):
#         Account.objects.get_or_create(user=kwargs.get('instance'))

# @receiver(post_save, sender=User)
# def create_account(sender, **kwargs):    
#     if kwargs.get('created', False):
#         Account.objects.get_or_create(account_name=kwargs.get('instance'))

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
