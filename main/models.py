from enum import unique
from django.db import models
from django.shortcuts import reverse
from django.contrib.sites.models import Site
# Create your models here.


class TestItem(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, )
    title = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

