# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
     
    path("societ/", views.societe, name="societ"),
    path("creation_de_societe/", views.Creation_de_societe,name="creation_de_societe"),
    #path("edite/<str:pk>/", views.Visualiser_societe,name="VisualiserSociete") , 
    path("Update/<str:pk>/", views.Edite_societe,name="Edite_societe") , 
    path("Delete/<str:pk>/", views.Delete_societe,name="Delete_societe") ,
    #path("societ/AffichageCard", views.AffichageCard, name="AffichageCard") ,
  

]

