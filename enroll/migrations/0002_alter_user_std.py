# Generated by Django 3.2.9 on 2021-12-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='std',
            field=models.CharField(max_length=20),
        ),
    ]
