"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib.auth import views as auth_views


from mainapp import views as portal_views

urlpatterns = [
    path( 'admin/', admin.site.urls ),
]

urlpatterns += [
    # path( '',          portal_views.index,     name='index' ),
    path( '',          auth_views.login, { 'template_name' : 'account/login.html' }, name='login' ),
    path( 'dashboard', portal_views.dashboard, name='dashboard' ),
    path( 'profile',   portal_views.profile,   name='profile' ),
]

# registration and login paths
urlpatterns += [
    path( 'login/',  auth_views.login, { 'template_name' : 'account/login.html' }, name='login' ),
    path( 'logout/', auth_views.logout, {'next_page': '/login'}, name='logout' ),
    path( 'signup/', portal_views.signup, name='signup' ),
    path( 'password_reset/',      auth_views.password_reset,      { 'template_name' : 'account/password_reset.html' },          name='password_reset' ),
    path( 'password_reset/done/', auth_views.password_reset_done, { 'template_name' : 'account/password_reset_done.html' },     name='password_reset_done' ),
    re_path( 'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        auth_views.password_reset_confirm,                        { 'template_name' : 'account/password_reset_confirm.html' },  name='password_reset_confirm' ),
    path( 'reset/done/', auth_views.password_reset_complete,      { 'template_name' : 'account/password_reset_complete.html' }, name='password_reset_complete' )
]
