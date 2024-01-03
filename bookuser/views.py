from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login,logout
from django.views.generic import FormView,View,UpdateView
from django.contrib.auth.views import LoginView
from bookuser.forms import UserRegistrationForm ,UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from transactions.views import send_email

# Create your views here.
class UserRegisterView(FormView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'user created successful.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'something went wrong try again later.')
        return super().form_invalid(form)

class UserLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        messages.success(self.request, 'user logged in successful')
        return reverse_lazy('home')

class UserLogoutView(View):
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('home')
        
class UserUpdateView(View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Profile updated successfully done')
            return redirect('home') 
        return render(request, self.template_name, {'form': form})
    
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        send_email(self.request.user, "", 'pass_change',  'Password Change Success Message', 'transactions/email_template.html')
        messages.success(self.request, 'Password changed successfully done')
        return super().form_valid(form)

    
    
    
