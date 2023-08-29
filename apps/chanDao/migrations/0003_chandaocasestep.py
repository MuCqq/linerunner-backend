# Generated by Django 3.1.2 on 2021-02-24 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chanDao', '0002_auto_20210223_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChanDaoCaseStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.CharField(max_length=3000, verbose_name='')),
                ('expect', models.CharField(max_length=3000, verbose_name='')),
                ('case_result', models.CharField(choices=[['unexecuted', 'unexecuted'], ['pass', 'pass'], ['fail', 'fail'], ['block', 'block']], default='unexecuted', max_length=3000, verbose_name='用例结果')),
                ('remarks', models.CharField(max_length=3000, verbose_name='')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chanDao.chandaocase')),
            ],
            options={
                'verbose_name': '阐道_用例步骤',
                'verbose_name_plural': '阐道_用例步骤',
                'db_table': 'fusion_chandao_step',
            },
        ),
    ]