from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.name}"


class District(models.Model):
    name = models.CharField(max_length=512)
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="districts",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-id']

