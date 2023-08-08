from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistertionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserUpdateForm, ImgUpdateForm


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


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        i_form = ImgUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and i_form.is_valid():
            u_form.save()
            i_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        i_form = ImgUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'i_form': i_form
    }

    return render(request, 'accounts/profile.html', context)

