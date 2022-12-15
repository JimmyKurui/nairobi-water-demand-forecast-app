# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WaterDataSql(models.Model):
    month = models.CharField(max_length=300, blank=True, null=True)
    average_wage = models.CharField(max_length=300, blank=True, null=True)
    population = models.CharField(max_length=300, blank=True, null=True)
    hh_size = models.CharField(max_length=300, blank=True, null=True)
    volume = models.CharField(max_length=300, blank=True, null=True)
    total_bill = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'water_data_sql'

class Prediction_save (models.Model):
    prediction_volume=models.FloatField(max_length=300,blank=True)