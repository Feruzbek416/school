# Generated by Django 4.1.3 on 2023-05-22 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0019_rename_zamdirektor_direktor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direktor',
            name='rasm',
        ),
    ]
