from django.urls import path
from app.views import list_users, add_user, save_user

urlpatterns = [
    path('', list_users, name='list_users'),
    path('add', add_user, name='add_user'),
    path('save', save_user, name='save_user'),
]
