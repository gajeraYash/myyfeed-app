from django.urls import path
from . import views


app_name = 'app'  # here for namespacing of urls.

urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.user_signup,name="signup"),
    path('signup/success',views.user_signup_success,name="signup-success"),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('feed',views.feed,name="feed"),
    path('user/search',views.user_search,name="user_search"),
    path('user/feed',views.user_feed,name="user_feed"),
] 