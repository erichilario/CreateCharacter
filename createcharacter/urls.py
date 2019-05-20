"""createcharacter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import logout
from django.contrib import admin
from creation import views as creation_views
#from creation.views import LoginView, LogoutView, CharactersView, DataModelView, DataDictionaryView, UserGuideView, signup
from creation.views import *
#from creation.views import IndexView


urlpatterns = [
    
    #path('', views.IndexView.as_view(), name='index'),
	#url(r'^$', index),
    url(r'^$', creation_views.IndexView.as_view(), name='index'), #https://stackoverflow.com/a/39207042
    url(r'^admin/', admin.site.urls),
    #url(r'^create/', include('creation.urls')),
    #url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', creation_views.signup, name='signup'),
    url(r'^login/$', creation_views.LoginView, name='login'),
    url(r'^logout/$', LogoutView, name='logout'),
    #url(r'^characters/', CharactersView.as_view(), name='characters'),
    url(r'^characters/', character_list_view, name='characters'),
    
    
    url(r'^data-model/', DataModelView.as_view(), name='data-model'),
    url(r'^data-dictionary', DataDictionaryView.as_view(), name='data-dictionary'),
    url(r'^user-guide/', UserGuideView.as_view(), name='user-guide'),
]
