# Generated by Django 3.1.1 on 2020-10-01 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200930_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='grade',
        ),
        migrations.AddField(
            model_name='students',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=8, verbose_name='性別'),
        ),
        migrations.AddField(
            model_name='students',
            name='seat_number',
            field=models.SmallIntegerField(default=0, verbose_name='座號'),
        ),
        migrations.AlterField(
            model_name='course_record',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.course', verbose_name='課程'),
        ),
        migrations.AlterField(
            model_name='course_record',
            name='course_order',
            field=models.SmallIntegerField(verbose_name='選課順序'),
        ),
        migrations.AlterField(
            model_name='course_record',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.students', verbose_name='學生'),
        ),
        migrations.AlterField(
            model_name='students',
            name='class_code',
            field=models.SmallIntegerField(help_text='填寫班別', verbose_name='班別'),
        ),
        migrations.AlterField(
            model_name='students',
            name='number',
            field=models.SmallIntegerField(verbose_name='學號'),
        ),
    ]
