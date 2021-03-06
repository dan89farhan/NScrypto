# Generated by Django 2.0.1 on 2018-01-27 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoclient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encryptdecrypt',
            name='asymmetric_tech',
            field=models.CharField(choices=[('des', 'des 8 bit  ')], default='des', max_length=100),
        ),
        migrations.AlterField(
            model_name='encryptdecrypt',
            name='symmetric_asymmetric',
            field=models.CharField(choices=[('symmetric', 'Symmetric Algo'), ('asymmetric', 'ASymmetric Algo')], default='symmetric', max_length=100),
        ),
        migrations.AlterField(
            model_name='encryptdecrypt',
            name='symmetric_tech',
            field=models.CharField(choices=[('ceaser cipher', 'Ceaser Ciper')], default='ceaser cipher', max_length=100),
        ),
    ]
