from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import logout
from django.contrib import admin
from creation import views
from creation.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls), #disabled for deployment
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', LoginView, name='login'),
    url(r'^logout/$', LogoutView, name='logout'),
    url(r'^characters/', character_list_view, name='characters'),
    url(r'^character/(?P<id>\d+)/$', CharacterView, name='character'),
    url(r'^edit/(?P<id>\d+)/$', CharacterEditView, name='edit'),
    url(r'^delete/(?P<id>\d+)/$', CharacterDeleteView, name='delete'),
    url(r'^create/$', CharacterCreateView, name='create'),
    url(r'^data-model/', DataModelView.as_view(), name='data-model'),
    url(r'^data-dictionary', DataDictionaryView.as_view(), name='data-dictionary'),
    url(r'^user-guide/', UserGuideView.as_view(), name='user-guide'),
]
