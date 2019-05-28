# Generated by Django 2.1.5 on 2019-04-01 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gpsschool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_subject', models.CharField(max_length=120)),
                ('standard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='standard_subjects', to='gpsschool.Standard')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='joining_date',
            field=models.DateField(auto_created=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_teaches', to='gpsschool.Teacher'),
        ),
        migrations.AddField(
            model_name='book',
            name='subjects',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='book_subject', to='gpsschool.Subject'),
            preserve_default=False,
        ),
    ]
