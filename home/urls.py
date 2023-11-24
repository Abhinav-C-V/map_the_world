from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
# from .views import UserLoginView, UserSignupView, ChangePasswordView, SignupOTPView, EmailChangeVerification

urlpatterns = [
    # path('', views.store, name='store'),
    path('', views.home, name='home'),
]