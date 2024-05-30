from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('urllogin', views.mylogin, name='loginpage'),
    path('urlregister', views.myregister, name='register'),
    path('urllogout', views.mylogout, name='logoutpage'),
    path('formregister', views.formregister, name='formregister'),
    path('formlogin', views.formlogin, name='formlogin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('boardpage', views.boardpage, name='boardpage'),
    path('formboard', views.formboard, name='formboard'),
    path('boardedit/<str:id>/', views.boardedit, name='boardedit'),
    path('formboardedit', views.formboardedit, name='formboardedit'),
    path('boarddelete/<str:id>/', views.boarddelete, name='boarddelete'),
    path('formboarddelete', views.formboarddelete, name='formboarddelete'),
    path('uploadimage', views.uploadimage, name='uploadimage'),
    path('formuploadimage', views.formuploadimage, name='formuploadimage'),
    path('viewboard', views.viewboard, name='viewboard'),
    path('lihatgambarpapan/<str:id>/', views.lihatgambarpapan, name='lihatgambarpapan'),
    path('formuploadgambarpapan', views.formuploadgambarpapan, name='formuploadgambarpapan'),
    path('hapusgambarpapan/<str:idimage>/<str:idboard>/', views.hapusgambarpapan, name='hapusgambarpapan'),
    path('hapusgambar/<str:id>/', views.hapusgambar, name='hapusgambar'),
    path('profil', views.profil, name='profil'),
    path('editprofil', views.edit_profil, name='editprofil'),
]
