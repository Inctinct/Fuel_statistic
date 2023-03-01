from django.db import models

# Create your models here.


class Firm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Fuel(models.Model):
    name = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Refueling(models.Model):
    adress = models.TextField()
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)

    def __str__(self):
        return self.adress

