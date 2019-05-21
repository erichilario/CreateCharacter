from django import forms
from .models import Character

class CharacterCreateForm(forms.ModelForm):
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