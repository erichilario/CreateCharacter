from django.forms import ModelForm, TextInput
from .models import Character

class CharacterCreateForm(ModelForm):
	class Meta:
		model = Character
		fields = (
			'character_name',
			'race',
			'job',
			'color',
			'hair',
			'face',
			'sex',
		)

class CharacterEditForm(ModelForm):
	class Meta:
		model = Character
		fields = (
			'character_name',
			'race',
			'job',
			'color',
			'hair',
			'face',
			'sex',
		)