'''
MakeMigrations: Makes a migration file
Migrate: Applies the migration to the database
Migrations are like a version control system for your database
'''
from django.db import models


class Treasure(models.Model):

    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10,
                                decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)

    class Meta:
            ordering = ['name']
            verbose_name='treasure'
            verbose_name_plural='treasures'

    def __str__(self):
    	return name

