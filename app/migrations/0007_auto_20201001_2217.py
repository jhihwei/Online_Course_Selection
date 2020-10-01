# Generated by Django 3.1.1 on 2020-10-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201001_2126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group_record',
            options={'verbose_name_plural': '志願分組'},
        ),
        migrations.AlterModelOptions(
            name='students',
            options={'ordering': ['class_code', 'seat_number'], 'verbose_name_plural': '學生'},
        ),
        migrations.AlterField(
            model_name='group_record',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], default='male', max_length=8, verbose_name='性別'),
        ),
    ]
