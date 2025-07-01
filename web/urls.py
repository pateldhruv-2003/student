from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path('', views.index),
    path('register', views.register,name='register'),
    path('login_view', views.login_view,name='login_view'),
    path('logout_view', views.logout_view,name='logout_view'),
    path('index', views.index,name='index'),
    path('about', views.about),
    path('contact1', views.contact1),
    path('base', views.base),
    path('showstudentlist',views.showstudentlist,name="showstudentlist"),
    path('showcategorylist',views.showcategorylist,name="showcategorylist"),
    path('showproductlist',views.showproductlist,name="showproductlist"),
    path('addstudent',views.addstudent,name="addstudent"),
    path('addproduct',views.addproduct,name="addproduct"),
    path('addcontact',views.addcontact,name="addcontact"),
    path('addfees',views.addfees,name="addfees"),
    path('showcontactlist',views.showcontactlist,name="showconatctlist"),
    path('showfeeslist',views.showfeeslist,name="showfeeslist"),
    path('delete_contact/<int:id>',views.delete_contact,name="delete_contact"),
    path('delete_student/<int:id>',views.delete_student,name="delete_student"), 
    path('delete_product/<int:id>',views.delete_product,name="delete_product"),
    path('delete_fees/<int:id>',views.delete_fees,name="delete_fees"),
    path('edit_contact/<int:id>',views.edit_contact,name="edit_contact"),
    path('edited_student/<int:id>',views.edited_student,name="edited_student"),
    path('editted_product/<int:id>',views.editted_product,name="editted_product"),
    path('showstudent',views.showstudent,name="showstudent"),
    path('studentdetail/<int:id>',views.studentdetail,name="studentdetail"),
]



