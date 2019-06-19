# Generated by Django 2.0.2 on 2019-04-22 21:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topic', '0005_auto_20190422_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='RightWrongSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_num', models.IntegerField(blank=True, default=0, null=True, verbose_name='正确率')),
                ('wrong_num', models.IntegerField(blank=True, default=0, null=True, verbose_name='错误率')),
                ('action', models.CharField(choices=[('1', '正确'), ('0', '错误')], default=1, help_text='对错类别', max_length=20, verbose_name='对错类别')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='right_wrong', to='topic.Subject', verbose_name='题目答案')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='答题者')),
            ],
            options={
                'verbose_name': '题目对错',
                'verbose_name_plural': '题目对错',
            },
        ),
    ]
