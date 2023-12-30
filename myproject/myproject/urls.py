from django.contrib import admin
from django.urls import path
from myapp import views as myapp
# from second_app import views as secondapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_create/',myapp.user_create,name='user_create'),
    path('log_in/',myapp.login,name='login'),
    path('token_verification/',myapp.token_verification,name='token_verification'),
    path('regd/',myapp.registration,name='regd'),
]
