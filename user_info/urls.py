from django.urls import path

from . import views

urlpatterns = [
    path('/<personal_user_id>', views.one_user_info_page),
]
