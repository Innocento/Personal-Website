""" This model will be used """

from django.db import models
from django.urls import reverse

# This model shows the status of work


class Work(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=100)
    date_started = models.DateField('start_project')
    date_finished = models.DateField('end_project', blank=True)

    def __str__(self):
        """String representing the Model object"""
        return self.name

    def get_absolute_url(self):
        """Retuns the url to access a detail record for this book"""
        return reverse('project_detail', args=[str(self.id)])
