from django.shortcuts import render, redirect
from .models import User


def show_login(request):
    return render(request, 'login.html')


def list_users(request):
    user_list = User.objects.all()
    context = {'userList': user_list}
    return render(request, 'list.html', context)
