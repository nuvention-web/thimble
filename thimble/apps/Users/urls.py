from django.conf.urls import patterns, include, url
from thimble.apps.Users.views import views
from django.contrib.auth.views import login, logout
from thimble.apps.Users.forms.forms import LoginForm

urlpatterns = patterns('',
	url(r'^login/$', login, {'template_name':'Users/login.html','authentication_form':LoginForm}, name='login'),
	url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
	url(r'^create-account/$', views.create_account, name='create_account'),
	url(r'^edit-account/(?P<user_type>[\w]+)/$', views.edit_account, name='edit_account'),
)
