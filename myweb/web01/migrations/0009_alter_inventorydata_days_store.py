# Generated by Django 3.2.1 on 2022-09-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web01', '0008_auto_20220910_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorydata',
            name='days_store',
            field=models.CharField(default=None, max_length=64, verbose_name='可持续天数'),
        ),
    ]
