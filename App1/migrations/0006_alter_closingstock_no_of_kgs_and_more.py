# Generated by Django 5.1 on 2024-09-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0005_alter_dailysales_balance_cash_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closingstock',
            name='no_of_kgs',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dailysales',
            name='balance_cash',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dailysales',
            name='curry_weight',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dailysales',
            name='expense',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dailysales',
            name='gpay',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dailysales',
            name='live_weight',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dailysales',
            name='total_sales_amount',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dailysheet',
            name='number_of_birds_purchase',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dailysheet',
            name='total_purchase_weight',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dailysheet',
            name='total_stock_weight',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dailysheet',
            name='total_weight',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='weeklyreport',
            name='average_weight',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='weeklyreport',
            name='rate',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='weeklyreport',
            name='total_amount',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='weeklyreport',
            name='total_kilograms',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
