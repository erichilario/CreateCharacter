from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
#from creation.models import Profile, Account, Character, Race, Job
from creation.models import Account, Character, Race, Job

class CharacterInstanceInline(admin.TabularInline):
	model = Character

class AccountAdmin(admin.ModelAdmin):
	inlines = [CharacterInstanceInline]

	def account_character_count(self,obj):
		return obj.character_set.count()

	account_character_count.short_description = "Character Count"
	list_display = ('user', 'id', 'account_character_count')
	ordering = ('id',)

class AccountInline(admin.StackedInline):
    model = Account
  
class CustomUserAdmin(UserAdmin):
    inlines = (AccountInline, )    
 
 
admin.site.unregister(User) # unregister User model
admin.site.register(User, CustomUserAdmin) # register User model with changes

#admin.site.register(Profile)
admin.site.register(Account, AccountAdmin)
admin.site.register(Character)
admin.site.register(Race)
admin.site.register(Job)
