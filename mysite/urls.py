"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from mainweb.views import mainpage1,CustomSignupView,edit_bio
from forums.views import create_forum_post, forum_page,forum_post_detail, get_comments, post_comment

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', mainpage1,name ="home"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),    
    path('add_info', edit_bio,name ="edit_bio"),
    path('forum/', forum_page, name='forum_page'),
    path('forum/create/', create_forum_post, name='create_forum_post'),
    path('forum/post/<slug:slug>/', forum_post_detail, name='forum_post_detail'),
    path('post/<slug:slug>/comments/', get_comments, name='get_comments'),
    path('post/<slug:slug>/comment/', post_comment, name='post_comment'),
]
