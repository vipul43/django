from django.urls import path
from . import views

#new views file added is to be pointed by a URLconf
#for that add that views function to the urlpatterns
#whenever a http request matching the urlpattern is made
#this URLconf matches it to views.index function
#thus running that specific function in that file
urlpatterns = [
    path('', views.index, name='index'),
    path('time/', views.getTime, name='getTime'),

]
