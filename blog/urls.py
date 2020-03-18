from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    # we will be passing blog_id into the view as a parameter
    # here it will pick the url and convert it to int
    # then pass it to views.detail
]
