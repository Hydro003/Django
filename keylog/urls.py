from django.urls import path
from . import views

urlpatterns = [
    path('log_keystroke/', views.log_keystroke, name='log_keystroke'),
]
