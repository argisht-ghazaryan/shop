from django.shortcuts import render, redirect
from .forms import UserForm


def register_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            user = form.save()
            user.profile.phone = phone
            user.ptofile.save()
            return redirect('home')
    return render(request, 'user/register.html', context={'form': form, })
