from django.urls import path
from account import views
from django.conf.urls import include

app_name = 'account'
urlpatterns = [
   path('register/', views.register, name='register'), 
   path('login/', views.login, name='login'),
   path('logout/', views.logout, name='logout'),
   path('', include('social_django.urls', namespace='social')),
]
