from django.db import models


class Color(models.Model):
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=50)
    summary = models.TextField(default='this is cool!')

    def __unicode__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=50)
    summary = models.TextField(default='this is cool!')
    product = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title
