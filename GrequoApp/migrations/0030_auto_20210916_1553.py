# Generated by Django 3.2.7 on 2021-09-16 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GrequoApp', '0029_alter_testoo_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userquest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.TextField(default='', max_length=300)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='testoo',
        ),
        migrations.DeleteModel(
            name='Userquestion',
        ),
    ]
