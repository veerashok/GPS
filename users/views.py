from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ContactForm
from gpsschool.models import Teacher, Student
from .models import ContactUs



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


@login_required
def profile(request):

    is_teacher = False

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    if hasattr(request.user, 'teacher'):
        is_teacher = True


    context = {
        'u_form': u_form,
        'p_form': p_form,
        'is_teacher': is_teacher,
    }

    return render(request, 'users/profile.html', context)


def contact_view(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            ContactUs.objects.create(name=request.POST['name'],
                email=request.POST['email'],
                message=request.POST['message']
                )
            messages.success(request, f'Your message has been sent. We would contact you as soon as possible!')
            form = ContactForm()


    else:
        form = ContactForm()

    return render(request, 'gpsfrontend/contact.html', { 'form': form })
