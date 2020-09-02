from django.contrib import admin
from django.urls import path, include
from users.views import UserListView, SignUpView, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('', UserListView.as_view(), name='home'),
    path('users/', include('users.urls')),
    path('', include('labs.urls')),
]
