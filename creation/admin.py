from django.contrib import admin
from creation.models import Account, Character, Race, Job

class CharacterInstanceInline(admin.TabularInline):
	model = Character

class AccountAdmin(admin.ModelAdmin):
	inlines = [CharacterInstanceInline]

	def account_character_count(self,obj):
		return obj.character_set.count()

	account_character_count.short_description = "Character Count"
	list_display = ('account_name', 'id', 'account_character_count')
	ordering = ('id',)

admin.site.register(Account, AccountAdmin)
admin.site.register(Character)
admin.site.register(Race)
admin.site.register(Job)
