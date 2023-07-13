from functools import wraps

from django.shortcuts import redirect


def own_user(func: callable):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk'):
            return redirect('home')
        return func(request, *args, **kwargs)
    return wrapper
