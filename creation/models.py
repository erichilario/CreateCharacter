from django.db import models

class Character(models.Model):
	character_name = models.CharField(max_length=12, default='randomname') #need a function that pulls "unused" names from a dictionary.txt
	character_image = models.ImageField() #this would depend on the class, race and attributes of the character e.g. orcbarb_m_a2 for orc barbarian male face a, feature 2
	account = models.ForeignKey(
		Account,
		on_delete=models.CASCASE,
		verbose_name="account character"
	)

	def __str__(self):
		return self.hero_name #must be unique

class Race(models.Model):
	race_name = models.CharField(max_length=20, default='Human')
	race_story = models.TextField(max_length=500, default='Description')
	character = models.ForeignKey(
		Character,
		on_delete=models.CASCADE,
		verbose_name="character race"
	)
	race_image = models.ImageField()

	def __str__(self):
		return self.race_name

class Class(models.Model):
	class_name = models.CharField(max_length=20, default='Barbarian')
	class_story = models.TextField(max_length=500, default='Description')
	character = models.ForeignKey(
		Character,
		on_delete=models.CASCASE,
		verbose_name="character class"
	)
	class_image = models.ImageField()

	def __str__(self):
		return self.class_name

class Account(models.Model):
	account_name = models.CharField(max_length=100, default='Account Name')
	account_password = models.CharField(max_length=100, default='Password')
	account_email = models.CharField(max_length=200, default='email@address.com')

	def __str__(self):
		return self.account_name