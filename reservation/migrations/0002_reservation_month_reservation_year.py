# Generated by Django 5.0.6 on 2024-06-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='month',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='year',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
