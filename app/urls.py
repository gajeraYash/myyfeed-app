from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('sign-up',views.signup),
    path('sign-up-form',views.signup_form_view),
]