from django.db import models

# Create your models here.


class Dealership(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Car(models.Model):

    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return "{0} at {1}".format(self.model.name, self.dealership.name)
