# Generated by Django 2.2.7 on 2019-11-05 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicken', '0002_chicken_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='chicken',
            name='image',
            field=models.FileField(blank=True, upload_to='images'),
        ),
    ]