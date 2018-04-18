from django.conf.urls import url
from . import views   
urlpatterns = [
	url(r'^$', views.index) # I tried ../time_display/ but "Not Found: /favicon.ico" error..???
	]