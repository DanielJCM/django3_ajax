# -*- coding: utf-8 -*-
from django.urls import path
from app import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('list', views.List.as_view(), name='list'),
    path('create/', views.Create.as_view(), name='create'),
    path('update/', views.Update.as_view(), name='update'),
    path('details/<int:pk>/', views.Detail.as_view(), name='details'),
    path('delete/', views.Delete.as_view(), name='delete'),
]
