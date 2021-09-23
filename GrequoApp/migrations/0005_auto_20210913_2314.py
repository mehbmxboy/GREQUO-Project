# Generated by Django 3.2.7 on 2021-09-13 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrequoApp', '0004_grequouser_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grequouser',
            name='user_id',
        ),
        migrations.AddField(
            model_name='grequouser',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1223, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grequouser',
            name='date_created',
            field=models.DateField(default=datetime.date.today),
        ),
    ]