from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        form.save()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('main-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})