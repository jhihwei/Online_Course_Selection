# Generated by Django 3.1.1 on 2020-10-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201001_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='class_code',
            field=models.SmallIntegerField(help_text='填寫數字代碼', verbose_name='班級'),
        ),
    ]
