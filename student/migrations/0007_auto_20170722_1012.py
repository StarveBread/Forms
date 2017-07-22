# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20170715_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=150)),
                ('subject_description', models.TextField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='detail',
            name='course',
        ),
        migrations.AddField(
            model_name='detail',
            name='course',
            field=models.ManyToManyField(related_name='Detail', to='student.Course'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ManyToManyField(related_name='Courses', to='student.Subject'),
        ),
    ]
