# Generated by Django 5.0.4 on 2024-04-18 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('dueDate', models.DateTimeField()),
                ('completed', models.BooleanField()),
                ('classId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoListApp.class')),
            ],
        ),
    ]