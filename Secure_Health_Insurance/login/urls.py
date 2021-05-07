from django.urls import path,re_path
from .views import SignUpView
from login import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # path('signin/', views.signin,name='signin'),
    url(r'login_success/$', views.login_success, name='login_success')
]


