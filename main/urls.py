from django.urls import path, include
from .views import index, forums, thread, forum, com, create, war

urlpatterns = [
    path('', index),
    path('forums/', forums),
    path('threads/<int:th_id>/', thread),
    path('comment/<int:th_id>/', com),
    path('forums/<int:fr_id>/', forum),
    path('forums/<int:fr_id>/create/', create),
    path('war/<int:ps_id>/', war),
    path('accounts/', include('django.contrib.auth.urls')),
]
