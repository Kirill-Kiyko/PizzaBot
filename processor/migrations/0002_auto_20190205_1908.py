# Generated by Django 2.1.3 on 2019-02-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='payment_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
