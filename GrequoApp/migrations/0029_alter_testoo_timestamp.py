# Generated by Django 3.2.7 on 2021-09-16 10:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GrequoApp', '0028_alter_testoo_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testoo',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
