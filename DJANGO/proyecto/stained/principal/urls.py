from .views import main_view, signup_view, my_recommendations_view, register_view
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', main_view, name='main-view'),
    path('signup/', signup_view, name='signup-view'),
    path('login/', LoginView.as_view(template_name='principal/login.html'), name='login'),
    path('profile/', my_recommendations_view, name='profile'),
    path('signup/profile/<str:wallet>', register_view, name='profile'),
    path('logout/', LogoutView.as_view(template_name='principal/main.html'), name='logout-view'),
    path('<str:ref_code>/', main_view, name='main-view'),
]