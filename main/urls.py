from django.urls import path, include
from .views import index, forums, thread, forum

urlpatterns = [
    path('', index),
    path('forums/', forums),
    path('threads/<int:th_id>/', thread),
    path('forums/<int:fr_id>/', forum),
    path('accounts/', include('django.contrib.auth.urls')),
]
