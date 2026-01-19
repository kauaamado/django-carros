from django.db import models

# Create your models here.

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, blank=False, null=False)
    brand = models.CharField(max_length=200, blank=False, null=False)
    factory_year = models.IntegerField(blank=True, null=False)
    model_year = models.IntegerField(blank=True, null=False)
    value = models.FloatField(blank=True, null=False)

    def __str__(self):
        return self.model