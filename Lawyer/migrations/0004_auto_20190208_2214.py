# Generated by Django 2.1.4 on 2019-02-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lawyer', '0003_auto_20190208_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyer',
            name='hcr_number',
            field=models.IntegerField(unique=True),
        ),
    ]
