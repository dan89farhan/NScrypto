# Generated by Django 2.0.1 on 2018-01-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoclient', '0002_auto_20180127_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encryptdecrypt',
            name='asymmetric_tech',
            field=models.CharField(choices=[('des', 'des 8 bit  ')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='encryptdecrypt',
            name='symmetric_tech',
            field=models.CharField(choices=[('ceaser cipher', 'Ceaser Ciper')], default='', max_length=100),
        ),
    ]
