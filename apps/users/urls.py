from django.urls import path
from .views import register_user, login_view, logout_view, profile_view, UserUpdateView, delete_user_view

app_name = 'users'
urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update'),
    path('delete/', delete_user_view, name='delete'),

]
