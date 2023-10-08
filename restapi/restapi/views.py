from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render 
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# C:\Users\Ramya\restapi\restapiapp\views.py

def homepage_view(request):
    return render(request, 'homepage.html')
