from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from helpers.own_decorators import own_user


class LoginRequiredMixin:
    @method_decorator(login_required)
    @method_decorator(own_user)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
