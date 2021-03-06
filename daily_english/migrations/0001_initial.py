# Generated by Django 2.0 on 2018-10-22 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyEnglish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_url', models.CharField(max_length=100, unique=True, verbose_name='图片链接')),
                ('created_time', models.DateField(max_length=20, verbose_name='图片原始时间')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('display', models.PositiveIntegerField(default=0, verbose_name='展示次数')),
            ],
            options={
                'verbose_name': 'DailyEnglish',
                'verbose_name_plural': 'DailyEnglish',
                'ordering': ['created_time'],
            },
        ),
        migrations.CreateModel(
            name='DailyImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='图名')),
                ('img_url', models.CharField(max_length=100, unique=True, verbose_name='图片链接')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('display', models.PositiveIntegerField(default=0, verbose_name='展示次数')),
            ],
            options={
                'verbose_name': 'DailyImg',
                'verbose_name_plural': 'DailyImg',
                'ordering': ['pub_time'],
            },
        ),
        migrations.CreateModel(
            name='DailyQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=100, verbose_name='每日一句')),
                ('note', models.CharField(max_length=200, unique=True, verbose_name='翻译')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('display', models.PositiveIntegerField(default=0, verbose_name='展示次数')),
            ],
            options={
                'verbose_name': 'DailyQuoto',
                'verbose_name_plural': 'DailyQuoto',
                'ordering': ['pub_time'],
            },
        ),
    ]
