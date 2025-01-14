# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include,re_path  # add this

urlpatterns = [ 
    re_path(r'', include("societ.urls")),
    re_path(r'', include("exercices.urls")), 
    re_path(r'', include("encaissements.urls")),
    re_path(r'', include("deductions.urls")),
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),            # UI Kits Html files
    
    
]
