from django.urls import path
from . import  views

urlpatterns = [
    path('',views.movie_list,name='movie_list'),
    path('add/',views.movie_add,name='movie_add'),
    path('edit/<int:pk>',views.movie_edit,name='movie_edit'),
    path('delete/<int:pk>',views.movie_delete,name='movie_delete'),
]