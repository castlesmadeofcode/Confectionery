from django.db import models


class VarietyFlavor(models.Model):

    variety = models.ForeignKey("Variety", on_delete=models.CASCADE)
    flavor = models.ForeignKey("Flavor", on_delete=models.CASCADE)
    toppings = models.CharField(max_length=150)
