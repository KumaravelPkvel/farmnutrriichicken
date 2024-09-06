# Generated by Django 5.1 on 2024-08-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_dailysales'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('day', models.CharField(max_length=10)),
                ('bird_type', models.CharField(max_length=50)),
                ('number_of_birds', models.IntegerField()),
                ('total_kilograms', models.DecimalField(decimal_places=2, max_digits=10)),
                ('average_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remarks', models.TextField()),
            ],
        ),
    ]
