from django.urls import path, include
from .views import index, forums, thread, forum, com, create, war, user, like, reg

urlpatterns = [
    path('', index),
    path('forums/', forums),
    path('threads/<int:th_id>/', thread),
    path('comment/<int:th_id>/', com),
    path('forums/<int:fr_id>/', forum),
    path('forums/<int:fr_id>/create/', create),
    path('war/<int:ps_id>/', war),
    path('user/<str:us_nik>/', user),
    path('like/<int:post_id>/', like),
    path('accounts/register', reg),
    path('accounts/', include('django.contrib.auth.urls')),
]
