from django.urls import path, include
# from django.contrib.auth.views import logout

from rest_framework_jwt.views import obtain_jwt_token,  refresh_jwt_token, verify_jwt_token
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('messages', views.MessageViewSet)

# router.register('users', views.UserViewSet)

router.register('entries', views.EntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', obtain_jwt_token, name="auth-login"),
    # path('auth/logout/', logout, name="auth-logout"),
    path('auth/register/', views.CreateUserView.as_view(), name="auth-register"),
    path('auth/token-refresh/', refresh_jwt_token),
    path('auth/token-verify/', verify_jwt_token),
    #    path('auth/validate-activation-code/$', views.ValidateActivationCode.as_view(), name="validate-activation-code"),
    #    path('auth/change-password/$', views.ChangePasswordView.as_view(), name="change-password"),
    #    path('auth/forgot-password/$', views.ForgotPasswordView.as_view(), name="forgot-password"),
]
