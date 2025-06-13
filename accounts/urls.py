from django.urls import path
from .views import RegistrationView, LoginView, register_page, login_page

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    # path('register-page', register_page, name='register_page'),
    # path('login-page', login_page, name='login_page'),
]
