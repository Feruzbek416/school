# Generated by Django 4.1.3 on 2023-05-20 15:01

import ap.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0009_udars_remove_uqituvchii_fan_remove_uqituvchii_theme_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uqituv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('img', models.ImageField(upload_to='image/')),
                ('job', models.CharField(max_length=150)),
                ('yil', models.CharField(max_length=150)),
                ('stafka', models.CharField(blank=True, choices=[('1stafka', '1Stafka'), ('yarim_stafka', 'Yarim Stafka')], max_length=30)),
                ('toifa', models.CharField(blank=True, choices=[('3', '3'), ('2', '2'), ('1', '1')], max_length=100)),
                ('fan', models.CharField(max_length=150)),
                ('video', models.FileField(upload_to='video/%y', validators=[ap.validators.file_size])),
                ('theme', models.CharField(max_length=999)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ap.authorr')),
            ],
        ),
        migrations.DeleteModel(
            name='Udars',
        ),
        migrations.DeleteModel(
            name='Uqituvchii',
        ),
    ]
