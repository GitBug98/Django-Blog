from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistertionForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegistertionForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegistertionForm()
    return render(request, 'accounts/Register.html', {'form': form})