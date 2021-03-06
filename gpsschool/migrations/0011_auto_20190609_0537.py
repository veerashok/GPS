# Generated by Django 2.1.5 on 2019-06-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsschool', '0010_auto_20190609_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(choices=[('01', 'Unit Test 1'), ('02', 'Unit Test 2'), ('03', 'Unit Test 3'), ('04', 'Unit Test 4'), ('05', 'Half Yearly'), ('06', 'Annual Exam'), ('07', 'Pre Board 1'), ('08', 'Pre Board 2')], max_length=2),
        ),
    ]
