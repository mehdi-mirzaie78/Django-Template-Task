from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.TitanicView.as_view(), name='titanic'),
    path('passengers/', views.PassengerCreateView.as_view(), name='passenger-create'),
    path('passengers/<int:pk>/', views.PassengerUpdateView.as_view(), name='passenger-update'),
    path('passengers/<int:pk>/delete/', views.PassengerDeleteView.as_view(), name='passenger-delete'),
    path('passengers/delete-all/', views.PassengerDeleteAllView.as_view(), name='passenger-delete-all'),
]
