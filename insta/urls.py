from django.contrib import admin
from django.urls import path
from insta import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("",views.home,name="home"),
    path("test",views.test,name="test"),
    path("login",views.login,name="login"),
    path("signin",views.signin,name="signin"),
    path("profile",views.profile,name="profile"),
    path("search",views.search,name="search"),

  
]
