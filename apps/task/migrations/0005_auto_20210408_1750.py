# Generated by Django 3.1.2 on 2021-04-08 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20210408_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testtask',
            name='task_name',
            field=models.CharField(max_length=200, verbose_name='任务标题'),
        ),
    ]
