from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Homework, SubmittedHomework, TodoItem, VideoTutorial, ContactSubmission
from .forms import TodoItemForm, ContactForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'The username or password is wrong. Please recheck it.')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def view_homeworks(request):
    submitted_homeworks = SubmittedHomework.objects.filter(student=request.user)
    homeworks = Homework.objects.filter(assigned_to=request.user).exclude(
        id__in=submitted_homeworks.values('homework_id')
    )
    return render(request, 'view_homeworks.html', {'homeworks': homeworks})

@login_required
def submit_homework(request):
    if request.method == 'POST':
        homework_id = request.POST.get('homework')
        homework_file = request.FILES.get('homework_file')
        
        if homework_id and homework_file:
            homework = Homework.objects.get(id=homework_id)
            SubmittedHomework.objects.create(
                homework=homework,
                student=request.user,
                file=homework_file
            )
            messages.success(request, 'Homework submitted successfully!')
            return redirect('view_homeworks')
        else:
            messages.error(request, 'Please select a homework and upload a file.')
    
    submitted_homeworks = SubmittedHomework.objects.filter(student=request.user)
    homeworks = Homework.objects.filter(assigned_to=request.user).exclude(
        id__in=submitted_homeworks.values('homework_id')
    )
    return render(request, 'submit_homework.html', {'homeworks': homeworks})

@login_required
def todo_list(request):
    todos = TodoItem.objects.filter(user=request.user).order_by('deadline')
    form = TodoItemForm()
    return render(request, 'todo_list.html', {'todos': todos, 'form': form})

@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    return redirect('todo_list')

@login_required
def update_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id, user=request.user)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'update_todo.html', {'form': form, 'todo': todo})

@login_required
@require_POST
def finish_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id, user=request.user)
    todo.delete()
    return JsonResponse({'status': 'success'})


@login_required
def video_tutorials(request):
    tutorials = VideoTutorial.objects.all().order_by('-created_at')
    return render(request, 'video_tutorials.html', {'tutorials': tutorials})



@login_required
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your query has been submitted successfully!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})


from django.contrib.auth import logout

def logout_view(request):
    logout(request)  # Logs out the current user
    return redirect('login')  # Redirects to your custom login view