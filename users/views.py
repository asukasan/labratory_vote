from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, RedirectView
from .models import CustomUser, Profile, Inquiry
from .forms import SignUpForm, InquiryForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(CreateView):
    model = CustomUser
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'ユーザーを作成しました。')
        return redirect('home')
            

class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'users/users.html'
    context_object_name = 'custom_user'

    def get_queryset(self):
        return self.model.objects.order_by('-num')

class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ('belongs1', 'belongs2', 'belongs3', 'rank')
    template_name = 'users/profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.user_profile

class InquiryView(LoginRequiredMixin, CreateView):
    model = Inquiry
    template_name = 'users/inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, '問合せのメッセージを管理者に送りました。')
        return super().form_valid(form)

class LoginView(TemplateView):
    template_name = 'registration/login.html'  
    form_class = LoginForm


        



def logout_view(request):
    logout(request)
    return redirect('login')