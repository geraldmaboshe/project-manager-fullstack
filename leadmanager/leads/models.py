# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    message = models.CharField(max_lenght=500, blank=True)
    created_at = models.DateField(auto_now_add=True)
