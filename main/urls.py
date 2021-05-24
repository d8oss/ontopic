from django.urls import path
from .views import index, forums, thread

urlpatterns = [
    path('', index),
    path('forums/', forums),
    path('threads/<int:th_id>/', thread),
]
