from django.urls import path
from . views import get_users, create_user, get_confeccion, create_confeccion, update_delete_confeccion

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('confecciones/', get_confeccion, name='get_confecciones'),
    path('confecciones/', create_confeccion, name='create_confecciones'),
    path('confecciones/<int:id>/', update_delete_confeccion, name='update_confeccion'),
]