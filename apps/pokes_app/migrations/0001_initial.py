# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 06:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('friends', models.ManyToManyField(related_name='_user_friends_+', to='pokes_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='poke',
            name='pokee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poked_by', to='pokes_app.User'),
        ),
        migrations.AddField(
            model_name='poke',
            name='poker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poked', to='pokes_app.User'),
        ),
    ]
