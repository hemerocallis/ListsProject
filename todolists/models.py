from django.db import models

# Create your models here.

class List(models.Model):
    '''to-do list'''
    pass

class Item(models.Model):
    '''to-do list item'''
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
