# Generated by Django 2.1.3 on 2019-02-05 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('size', models.CharField(max_length=200)),
                ('payment_type', models.CharField(max_length=200)),
            ],
        ),
    ]
