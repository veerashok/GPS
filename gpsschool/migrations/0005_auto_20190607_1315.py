# Generated by Django 2.1.5 on 2019-06-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsschool', '0004_auto_20190607_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentschedule',
            name='transactions',
            field=models.ManyToManyField(related_name='user_transactions', to='gpsschool.Payments'),
        ),
    ]