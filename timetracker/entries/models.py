from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Project(models.Model):
    client = models.ForeignKey('Client')
    name = models.CharField(max_length=200)

    def __str__(self):
        return '<{}> {}'.format(self.client, self.name)

class WorkPeriod(models.Model):
    start = models.DateTimeField(default=timezone.now)
    stop = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '[{} - {}]'.format(self.start, self.stop)

class Entry(models.Model):
    project = models.ForeignKey('Project')
    work_period = models.ForeignKey('WorkPeriod', null=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return '{} ({}) {}'.format(self.work_period, self.project, self.description)

    def is_finished(self):
        return self.stop is not None
