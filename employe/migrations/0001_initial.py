# Generated by Django 5.0.3 on 2024-03-14 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curds', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneno', models.CharField(max_length=15)),
                ('job_description', models.CharField(max_length=100)),
                ('bio', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='curds.curd')),
            ],
            options={
                'db_table': 'employe',
            },
        ),
        migrations.CreateModel(
            name='SalaryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_sal', models.CharField(max_length=10)),
                ('epf', models.CharField(max_length=10)),
                ('net_sal', models.CharField(max_length=10)),
                ('employee', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='employe.employeemodel')),
            ],
            options={
                'db_table': 'salary',
            },
        ),
    ]
