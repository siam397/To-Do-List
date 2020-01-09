from django.contrib import admin
from django.urls import path
from todolist import views
urlpatterns = [
    path('',views.todo,name='home'),
    path('addtodo/',views.addtodo),
    path('deletetodo/<int:todolist_id>/',views.deletetodo),
]