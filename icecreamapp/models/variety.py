from django.db import models
from django.urls import reverse


class Variety(models.Model):

    name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    flavors = models.ManyToManyField("Flavor", through='VarietyFlavor')

    class Meta:
        verbose_name = ("Variety")
        verbose_name_plural = ("Varieties")

    def __str__(self):
        return f"{self.name} ({self.country_of_origin})"

    def get_absolute_url(self):
        return reverse("Variety_detail", kwargs={"pk": self.pk})
