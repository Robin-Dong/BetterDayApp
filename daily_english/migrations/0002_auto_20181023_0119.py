# Generated by Django 2.0 on 2018-10-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_english', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyimg',
            name='img_url',
            field=models.CharField(max_length=200, unique=True, verbose_name='图片链接'),
        ),
    ]