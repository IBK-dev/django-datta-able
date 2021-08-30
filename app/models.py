# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class société(models.Model):
    RAISON_SOCIALE = models.CharField('RAISON SOCIALE', max_length=120)
    Nom = models.CharField('Nom', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    class Meta: 
        db_table="société"

