# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 03:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('steam_id', models.CharField(max_length=20)),
                ('team_choices', models.CharField(choices=[('DUOS', 'DUOS'), ('SQUADS', 'SQUADS'), ('DUOS FPS', 'DUOS FPS'), ('SQUADS FPS', 'SQUADS FPS')], max_length=10)),
                ('region_choices', models.CharField(choices=[('NA', 'North America'), ('EU', 'Europe'), ('AS', 'Asian'), ('OC', 'Oceania'), ('SA', 'South America'), ('SEA', 'South East Asia'), ('KR/JP', 'Korea/Japan')], max_length=5)),
                ('email', models.CharField(max_length=40)),
                ('has_profile', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
               ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
               ('bio', models.TextField(blank=True, max_length=500)),
               ('location', models.CharField(blank=True, max_length=30)),
               ('birth_date', models.DateField(blank=True, null=True)),
               ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
           ],
        ),

    ]
