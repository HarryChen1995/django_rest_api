from django.urls import path
from .views import *




urlpatterns = [
    path("", login_user, name = "login"),
    path("signup",  signup , name = "singup"),
    path("logout",  logout_user , name = "logout"),
    path("checklogin", checklogin, name = "checklogin")
]