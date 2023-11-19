from django.urls import path
from users import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('log_in/', views.LoginView.as_view(), name='log_in'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
