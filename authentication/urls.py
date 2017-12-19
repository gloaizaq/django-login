from django.conf.urls import url
from authentication import views
from django.contrib.auth import views as auth_views

app_name = "authentication"
urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/auth/login/'} , name='logout'),
    url(r'^welcome/$', views.WelcomeTemplateView.as_view(), name='welcome'),

]
