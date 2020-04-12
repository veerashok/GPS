# Generated by Django 2.1.5 on 2019-06-09 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpsschool', '0011_auto_20190609_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='standard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gpsschool.Standard'),
        ),
        migrations.AlterField(
            model_name='task',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gpsschool.Student'),
        ),
    ]