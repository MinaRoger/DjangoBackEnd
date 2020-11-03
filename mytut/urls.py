"""mytut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view
from pages.views import login_view
from pages.views import registration_view
from rest_framework import routers
from products.views import ProductViewSet
from products.views import ColorViewSet

from accounts.views import RegisterAPI
from accounts.views import LoginAPI,SocialLoginView
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'color', ColorViewSet)

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path('login/', LoginAPI.as_view(), name='login'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('logins/', login_view, name='logins'),
    path('oauth/login/', SocialLoginView.as_view()),
    path('api/auth/oauth/', include('rest_framework_social_oauth2.urls')),
    path('social_auth/', include(('social_auth.urls', 'social_auth'),
                                 namespace="social_auth")),


]
