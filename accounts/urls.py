from django.urls import path
from .views import signup_view, login_view, logout_view, home_view, content_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('logout/', logout_view, name='logout'),  # Logout URL
    path('content/', content_view, name='content'),
]
