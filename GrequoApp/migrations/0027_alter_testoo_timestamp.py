# Generated by Django 3.2.7 on 2021-09-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrequoApp', '0026_alter_testoo_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testoo',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]