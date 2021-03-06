# Generated by Django 3.2.7 on 2021-09-19 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GrequoApp', '0042_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likepost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_liked', models.NullBooleanField()),
                ('is_disliked', models.NullBooleanField()),
                ('like_count', models.PositiveSmallIntegerField(default=0)),
                ('dislike_count', models.PositiveSmallIntegerField(default=0)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GrequoApp.userquest')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
