from django.urls import path
from . import views

#new views file added is to be pointed by a URLconf
#for that, add the views function to the urlpatterns
#whenever a http request matching the urlpattern is made
#this URLconf matches it to views.index function
#thus running that specific function in that file

#namespacing polls app
app_name = 'polls'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('time/', views.getTime, name='getTime'),

    #adding more URLconf's for the functions in views
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote")
]
