from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.http import JsonResponse
# Create your views here.

def signup(request):

    if request.method == 'GET':

        return render(request,'signup.html', {'form' : UserCreationForm})   

    else: 
        if request.POST['senha1'] == request.POST['senha2']:
            if request.POST['senha1'] == '' or request.POST['senha2'] == '' or request.POST['username'] == '' or request.POST['email'] == '':
                return render (request,'signup.html', { 'form' : UserCreationForm ,"error": 'Preencha todos os campos'})
            try: 
                
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['senha1'], email=request.POST['email'])
                user.save()
                
                login(request, user)
               
                return redirect('tasks')
                
            except:
                return render (request,'signup.html', { 'form' : UserCreationForm ,"error": 'Usuário já existe'}) 
           
        return render (request,'signup.html', { 'form' : UserCreationForm ,"error": 'Senhas são diferentes'}) 

def home(request):
    return render(request,'home.html')



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
        
@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request,'tasks.html', {'tasks' : tasks})

@login_required
def task_detalhes(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request,'task_detalhes.html', {'task' : task, 'form' : form})

    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')

        except ValueError:
            return render(request,'task_detalhes.html', {'task' : task, 'form' : form, 'error' : 'Erro ao atualizar uma tarefa'})
        

@login_required
def completed_tarefa(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')


@login_required
def deleted_tarefa(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

@login_required
def exibir_tarefas_completadas(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request,'tasks.html', {'tasks' : tasks})


@login_required
def mark_task_completed(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        
        return redirect('tasks')  # Redirecione de volta para a lista de tarefas pendentes (incompletas)
    
    return JsonResponse({'message': 'Método inválido'}, status=405)


@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'completed_tasks.html', {'tasks': tasks})
