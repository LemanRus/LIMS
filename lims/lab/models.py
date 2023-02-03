from django.db import models


class Reagent(models.Model):
    name = models.CharField(max_length=200)
    made_by = models.CharField(max_length=200)
    made_date = models.DateField(blank=True, null=True)
    best_before = models.DateField(blank=True, null=True)



class Methodic(models.Model):
    name = models.CharField(max_length=200)
    acts_from = models.DateField(blank=True, null=True)
    acts_to = models.DateField(blank=True, null=True)
    used_reagents = models.ManyToManyField(Reagent, blank=True, related_name='methodics')



