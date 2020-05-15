from django.db import models
from django.urls import reverse


class Flavor(models.Model):

    name = models.CharField(max_length=100)
    alcohol_percent = models.IntegerField()
    varieties = models.ManyToManyField("Variety", through='VarietyFlavor')

    class Meta:
        verbose_name = ("Flavor")
        verbose_name_plural = ("Flavors")

    def __str__(self):
        return f"{self.name} ({self.alcohol_percent})"

    def get_absolute_url(self):
        return reverse("Flavor_detail", kwargs={"pk": self.pk})
