# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views


urlpatterns = [
     
    path("periodes_creat/", views.periodescreation, name="periodes_creat"),
    path("edition_periodes/<str:pk>/", views.Edite_periode, name="Edite_periodes"),
    path("Delete_periodes/<str:pk>/", views.Delete_periode,name="Delete_periode"),
    path("exercices/", views.periodess, name="periodes"),
    
    
    #path("edite/<str:pk>/", views.Visualiser_societe,name="VisualiserSociete") , 
    #path("Update/<str:pk>/", views.Edite_societe,name="Edite_societe") , 
    
    #path("societ/AffichageCard", views.AffichageCard, name="AffichageCard") ,
  

]

