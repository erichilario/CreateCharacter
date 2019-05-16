from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Account, Character, Race, Job

class IndexView(generic.ListView):
	template_name = 'landingpage.html'

class DataModelView(TemplateView):
	template_name = 'data-model.html'

def index(request):
	#html_var = 'hi'
	return render(request, "base.html", {"html_var": True})
	#return HttpResponse("Create index")

def signup(request):
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