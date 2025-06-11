from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('add_student/',views.add_student,name='add_student'),
    path('display_students/',views.display_students,name='display_students'),
    path('delete_student/<id>',views.delete_student,name='delete_student'),
    path('update_student/<id>',views.update_student, name='update_student')
]