# Generated by Django 5.0.4 on 2024-04-22 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LifeCaseModel',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('cito', models.BooleanField()),
                ('patient_id', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='SelectedPreviousCases',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('value', models.UUIDField()),
                ('lifecase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_previous_cases', to='lab.lifecasemodel')),
            ],
        ),
    ]
