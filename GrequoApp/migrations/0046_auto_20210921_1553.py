# Generated by Django 3.2.7 on 2021-09-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrequoApp', '0045_auto_20210921_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquest',
            name='dislike_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userquest',
            name='like_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
