# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)


class RecipeBook(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField()


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image = models.URLField()
    tags = models.ManyToManyField(Tag)
    recetario = models.ForeignKey(RecipeBook)


class Ingredient(models.Model):
    text = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe)





