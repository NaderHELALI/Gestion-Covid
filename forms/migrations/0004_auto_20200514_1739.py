# Generated by Django 3.0.5 on 2020-05-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20200514_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demande',
            name='item',
        ),
        migrations.AddField(
            model_name='demande',
            name='items',
            field=models.ManyToManyField(to='forms.Item'),
        ),
    ]
