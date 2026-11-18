from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from restaurant.views import home, register

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("restaurant.urls")),
    path("api/auth/register/", register, name="register"),
    path("api/auth/token/login/", obtain_auth_token, name="api_token_login"),
]
