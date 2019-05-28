from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm



def userHome(request):

	template_name = 'users/user.html'

	form = UserCreationForm()

	if request.method == "POST":
		
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
	else:

		form = UserCreationForm()

	return render(request, template_name, {'form': form})
