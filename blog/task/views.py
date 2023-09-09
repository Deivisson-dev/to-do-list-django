from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.POST['senha1'] == request.POST['senha2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['senha1'])
                user.save()

                login(request, user)
                return redirect('task')
            except:
                return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'Usuário já existe'})
        return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'Senhas não conferem'})