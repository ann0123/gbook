# Generated by Django 3.1.1 on 2020-12-10 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=15, verbose_name='姓名')),
                ('receiver', models.CharField(blank=True, default='公開', max_length=15, null=True, verbose_name='收件人')),
                ('subject', models.CharField(max_length=50, verbose_name='主旨')),
                ('content', models.TextField(verbose_name='內容')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='留言時間')),
            ],
        ),
    ]