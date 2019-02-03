from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('',views.ProfileDetail.as_view(), name='profile-detail'),
    path('update/',views.ProfileUpdate.as_view(), name='profile-update'),
    path('todos/', views.KeywordList.as_view(), name='keywords-list'),
]
