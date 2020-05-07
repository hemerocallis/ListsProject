from django.db import models

# Create your models here.
class Item(models.Model):
    '''to-do list item'''
    text = models.TextField(default='')
