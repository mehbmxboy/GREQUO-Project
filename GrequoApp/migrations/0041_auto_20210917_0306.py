# Generated by Django 3.2.7 on 2021-09-16 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GrequoApp', '0040_alter_usercomment_comment_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercomment',
            options={'ordering': ['timestamp']},
        ),
        migrations.AlterField(
            model_name='usercomment',
            name='comment_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]