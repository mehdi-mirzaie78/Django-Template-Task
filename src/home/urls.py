from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.TitanicView.as_view(), name='titanic'),
]