from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskForm


# Create your views here.

# Home do Projeto

def home(request):
    return render(request,'home.html')


def signup(request):

    if request.method == 'GET':

        return render(request,'signup.html', {'form' : UserCreationForm})   

    else: 
        if request.POST['senha1'] == request.POST['senha2']:

            try: 
                
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['senha1'])
                user.save()
                
                login(request, user)
               
                return redirect('tasks')
                
            except:
                return render (request,'signup.html', { 'form' : UserCreationForm ,"error": 'Usuário já existe'}) 
           
        return render (request,'signup.html', { 'form' : UserCreationForm ,"error": 'senhas são diferentes'}) 

def signin(request):

    if request.method == 'GET':
        return render(request,'signin.html', {'form': AuthenticationForm})

    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['senha'])

        if user is None:
            return render(request, 'signin.html', {'form' : AuthenticationForm,'error': 'Usuário ou senha está incorreto'})

        else:
                login(request, user)
                return redirect('tasks')    


@login_required   
def sair(request):
    logout (request)
    return redirect('home')

@login_required       
def tasks(request):
    return render(request,'tasks.html')

@login_required
def create_tasks(request):

    if request.method == 'GET':
        return render(request,'create_tasks.html', {'form' : TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')

        except ValueError:
            return render(request,'create_tasks.html', {'form' : TaskForm, 'error' : 'Dados incorretos'})