from authentication import views

from django.urls import path

urlpatterns=[
    path('register',views.RegisterAPIView.as_view(),name='register'),
    path('login',views.LoginAPIView.as_view(),name='login'),
    path('user',views.AuthuserAPIView.as_view(),name='login'),
    # path('logout',views.LogoutAPIView.as_view(),name='logout'),
]