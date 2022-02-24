from venv import create
from django.urls import include, path
from django.contrib import admin
from .views import createtask,Deletetask,Updatetask,taskDetail
from task import views

urlpatterns =[

    path('add/', createtask.as_view()),
     path('view/',views.index),
    path('<pk>/delete/',Deletetask.as_view()),
     path('<pk>/update/',Updatetask.as_view()),
    path('<pk>/view/',taskDetail.as_view()),
]
