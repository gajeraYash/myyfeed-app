from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'  # here for namespacing of urls.

urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.user_signup,name="signup"),
    path('signup/success',views.user_signup_success,name="signup-success"),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('feed',views.user_feed,name="feed"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)