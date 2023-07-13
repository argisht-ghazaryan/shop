from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView

from helpers.mixins import LoginRequiredMixin
from .forms import UserForm, UserUpdateForm
from .models import Profile
from ..product.models import Product


def register_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            category = form.cleaned_data.get('category')
            user = form.save()
            user.profile.phone = phone
            user.profile.category = category
            user.profile.save()
            messages.success(request, f'User with {user.username} username created successfully')
            return redirect('home')
    return render(request, 'users/register.html', context={'form': form, 'title': 'REGISTER PAGE'})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('home')
    return render(request, 'users/login.html', {'title': 'LOGIN PAGE'})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Successfully loging out')
    return redirect('home')


def profile_view(request):
    if request.user.is_authenticated:
        user = request.user
        product = Product.objects.filter(owner=user)
        profile = Profile.objects.filter(user=user)
    else:
        return redirect('login')
    return render(request, 'users/profile.html', context={'profile': profile, 'title': 'Profile Page',
                                                          'product': product})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_form_kwargs(self):
        user = self.get_object()
        kwargs = super().get_form_kwargs()
        kwargs.update({'initial': {'phone': user.profile.phone,
                                   'photo': user.profile.photo}})
        return kwargs

    def form_valid(self, form):
        user = self.get_object()
        phone = form.cleaned_data.get('phone')
        photo = form.cleaned_data.get('photo')
        user.profile.phone = phone
        user.profile.photo = photo
        user.profile.save()
        return super().form_valid(form)


# class UserDeleteView(DeleteView):
#     model = User
#     success_url = '/'
#     template_name = 'users/delete.html'


def delete_user_view(request):
    user = request.user
    if request.method == 'POST' and request.user == user:
        user.delete()
        return redirect('home')
    return render(request, 'users/delete.html', context={'title': f'DELETE{user.username}'})
