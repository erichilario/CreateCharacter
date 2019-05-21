from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CharacterCreateForm
from django.contrib.auth.views import logout

#from .models import Profile, Account, Character, Race, Job
from .models import Account, Character, Race, Job

class IndexView(generic.ListView):
	template_name = 'landingpage.html'
	model = Account

# class CharactersView(TemplateView):
# 	template_name = 'characters.html'

def character_list_view(request):
	if not request.user.is_authenticated():
		return redirect('/login/')

	queryset = Character.objects.filter(account__user=request.user)
	context = {
		"object_list": queryset
	}
	return render(request, "characters.html", context)

class DataModelView(TemplateView):
	template_name = 'data-model.html'

# def index(request):
# 	#html_var = 'hi'
# 	return render(request, "base.html", {"html_var": True})
# 	#return HttpResponse("Create index")

class DataDictionaryView(TemplateView):
	template_name = 'data-dictionary.html'

class UserGuideView(TemplateView):
	template_name = 'user-guide.html'

def LogoutView(request):
	template_name = 'logout.html'
	logout(request)
	return render(request,'landingpage.html')

def signup(request):
	if request.user.is_authenticated():
		#return redirect('creation:admin')
		return redirect('/')

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})

def LoginView(request):
	if request.user.is_authenticated():
		#return redirect('creation:admin')
		return redirect('/')
 
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
 
		if user is not None:
			# correct username and password login the user
			login(request, user)
			#return redirect('creation:user_details')
			return redirect('/')

 
		else:
			messages.error(request, 'Error wrong username/password')
 
	return render(request, 'login.html')

def CharacterView(request, id, slug):
	character = Character.objects.get(id=id)
	context = {
		'c': character,
	}
	return render(request, 'detail.html', context)

def CharacterCreateView(request):
	if request.method == 'POST':
		form = CharacterCreateForm(request.POST)
		if form.is_valid():
			character = form.save(commit=False)
			character.author = request.user
			character.save()
	else:
		form = CharacterCreateForm()
	context = {
		"form": form,
	}
	return render(request, 'create.html', context)