from django.db import models

# Create your models here.
class FertilizerRecommender(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    moisture = models.FloatField()
    nitrogen = models.FloatField()
    potassium = models.FloatField()
    phosphorus = models.FloatField()
    soil_type = models.CharField(max_length=100)
    crop_type = models.IntegerField()


class CropRecommender(models.Model):
    N = models.FloatField()
    P = models.FloatField()
    K = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()