from django.shortcuts import render


def home(request):
    template_name = 'gpsschool/signup.html'
    context = {}
    return render(request, template_name, context)


def profile(request):
	template_name = 'profiles/profile.html'
	context = {}
	return render(request, template_name, context)
