from django.urls import path

from . import views

urlpatterns = [
    path('/user_reg', views.user_registration),
    path('/user_log_in', views.user_authorization),
]
