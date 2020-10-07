from django.urls import path
from . import views

app_name = 'app'  # here for namespacing of urls.

urlpatterns = [
    path('',views.index,name="index"),
    path('sign-up',views.signupForm,name="signup"),
    path('sign-up-test',views.signup),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('feed',views.user_feed,name="feed"),
]