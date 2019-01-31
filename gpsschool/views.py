from django.shortcuts import render


def home(request):
    template_name = 'gpsschool/base.html'
    context = {}
    return render(request, template_name, context)
