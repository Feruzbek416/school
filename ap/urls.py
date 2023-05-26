from django.urls import path
from .views import *
urlpatterns = [
    path('',Maktab,name='home'),
    path('about/',about,name='about'),
    path('contact/',Aloqaga,name='contact'),
    path('bizning_faxr/',bizning,name='courses'),
    path('login/',Signin,name='login'),
    path('bizning_faxr/<str:name>/playlist',playlist,name='playlist'),
    path('profile/',direktor,name='profile'),
    path('register/',Register,name='register'),
    path('teachers/<str:name>/teacher_profile/',teacher_profile,name='teacher_profile'),
    path('teachers/',teacher,name='teachers'),
    path('update/',Maktab11,name='update'),
    path('watch-video/',Maktab12,name='watch-video'),
]