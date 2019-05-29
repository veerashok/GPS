from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from gpsschool.models import Teacher, Student


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):

    context = {}

    if hasattr(request.user, 'teacher'):
        obj = Teacher.objects.filter(user=request.user).first()
        context = {'object': obj, 'user_type': {'teacher': True, 'student':False,}}

    elif hasattr(request.user, 'student'):
        obj = Student.objects.filter(user=request.user).first()
        context = {'object': obj, 'user_type': {'teacher': False, 'student':True}}

    return render(request, 'users/profile.html', context)