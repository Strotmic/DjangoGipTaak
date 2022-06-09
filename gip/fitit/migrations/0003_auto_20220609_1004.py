# Generated by Django 2.2.5 on 2022-06-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitit', '0002_auto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horloge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=256)),
                ('horloge_pic', models.ImageField(blank=True, upload_to='car_pics')),
                ('materiaal', models.CharField(max_length=256)),
                ('prijs', models.FloatField()),
                ('merk', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='Auto',
        ),
    ]
