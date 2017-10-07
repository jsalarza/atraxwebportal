from django.conf.urls import url
from . import views

app_name = 'webportal'

urlpatterns = [

    #Dashboard
    url(r'^$', views.index, name='index'),

    #Terms and Condition
    url(r'^terms/$', views.termsandcondition, name='terms'),

    #Registration
    url(r'^register/$', views.register, name='register'),

    #Login
    url(r'^login/$', views.LoginForm, name='login'),

    #Homepage
    url(r'^homepage/$', views.homepage, name='homepage'),

    #Logout
    url(r'^logout/$', views.logout_user, name='logout')
]
