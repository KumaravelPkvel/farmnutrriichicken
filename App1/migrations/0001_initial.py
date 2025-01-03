# Generated by Django 5.1 on 2024-08-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClosingStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('day', models.CharField(max_length=50)),
                ('bird_type', models.CharField(choices=[('BROILER', 'Broiler'), ('CC', 'CC'), ('ORIGINAL', 'Original'), ('QUAIL', 'Quail')], max_length=10)),
                ('no_of_birds', models.PositiveIntegerField()),
                ('no_of_kgs', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mortality', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DailySheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('day', models.CharField(max_length=50)),
                ('bird_type', models.CharField(max_length=50)),
                ('number_of_birds_stock', models.PositiveIntegerField()),
                ('number_of_birds_purchase', models.FloatField()),
                ('total_birds', models.PositiveIntegerField()),
                ('total_stock_weight', models.FloatField()),
                ('total_purchase_weight', models.FloatField()),
                ('total_weight', models.FloatField()),
            ],
        ),
    ]
