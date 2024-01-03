from django.urls import path
from bookuser.views import UserRegisterView,UserLoginView,UserLogoutView,UserUpdateView,UserPasswordChangeView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/password_change/', UserPasswordChangeView.as_view(), name='password_change'),
]