from django.contrib import admin
from django.urls import path
from DjangoProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('location/', views.location, name="location"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('requests/', views.requests, name="requests"),
    path('responses/', views.responses, name="responses"),
    path('critique/', views.critique, name="critique"),
    path('delcontact/<int:id>', views.delcontact, name='delcontact'),
    path('delreview/<int:id>', views.delreview, name='delreview'),
    path('upcontact/<int:id>', views.upcontact, name='upcontact'),
    path('upreview/<int:id>', views.upreview, name='upreview'),

]
