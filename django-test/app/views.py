from django.shortcuts import render, redirect
from .models import User


def list_users(request):
    user_list = User.objects.all()
    context = {'userList': user_list}
    return render(request, 'user/list.html', context)


def add_user(request):
    context = {'user': User()}
    return render(request, 'user/add.html', context)


def save_user(request):
    user = User(name=request.POST['name'], email=request.POST['email'])
    user.save()
    return redirect('list_users')
