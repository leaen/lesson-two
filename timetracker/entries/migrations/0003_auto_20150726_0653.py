# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


def retain_work_periods(apps, schema_editor):
    Entry = apps.get_model("entries", "Entry")
    WorkPeriod = apps.get_model("entries", "WorkPeriod")
    for entry in Entry.objects.all():
        workPeriod = WorkPeriod(start=entry.start, stop=entry.stop)
        workPeriod.save()
        entry.workPeriod = workPeriod
        entry.save()

class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20150723_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WorkPeriod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('stop', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='workPeriod',
            field=models.ForeignKey(to='entries.WorkPeriod', null=True),
        ),
        migrations.RunPython(retain_work_periods),
        migrations.RemoveField(
            model_name='entry',
            name='start',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='stop',
        ),
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(to='entries.Client'),
        ),
    ]
