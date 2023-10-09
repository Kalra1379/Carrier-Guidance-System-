
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('homepage/',views.homepage,name= "homepage"),
    path('result1/', views.result1,name= "result1"),
    path('result/', views.result,name= "result"),
   path('',views.home,name= "home"),
   path('user/login', views.login,name="login"),
   path('user/signup' , views.signup,name="signup"),
   path("final1",views.final1,name="final1"),
   path("final",views.final,name="final"),
   path("final2",views.final2,name="final2"),
    path("final3",views.final3,name="final3"),
    path("Ebooks",views.Ebooks,name="Ebooks"),
    path("test",views.test,name="test"),
    path( "ml/",views.ml,name='ml'),
    path("about",views.about, name='about'),
    path('quiz',views.quiz,name="quiz"),
    path('predict', views.predict, name='predict'),
    path('contact',views.contact,name='contact'),
    # path('article',views.article,name='article')
]
