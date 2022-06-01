from django.urls import path
from login import views

urlpatterns = [
    #path("login/<name>",views.login_data, name='login_data'),
    path("login",views.login_user,name="login_user"),
    path("",views.home, name="home"),
    
]
