# Generated by Django 2.2.4 on 2019-12-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_auto_20191204_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetails',
            name='approved',
            field=models.BooleanField(default='True'),
        ),
    ]