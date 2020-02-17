from django.urls import path
from . import views

app_name = 'top'
urlpatterns = [
  path('', views.index, name='index'),
  path('wallet', views.wallet, name='wallet'),
  path('photo', views.photo, name='photo'),
]