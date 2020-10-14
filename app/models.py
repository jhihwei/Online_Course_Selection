from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import SmallIntegerField
from datetime import datetime    
# Create your models here.


class Course(models.Model):
    name_code = models.CharField(max_length=2, verbose_name="組別", default='Z')
    name = models.CharField(max_length=30, verbose_name="名稱")
    description = models.TextField(verbose_name="描述", default="無")

    def __str__(self):
        return '' + self.name

    class Meta:
        ordering = ['id']
        verbose_name_plural = '課程'


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12, verbose_name="姓名")
    number = models.IntegerField(verbose_name="學號")
    gender = models.CharField(max_length=8, verbose_name="性別", default='male',
                              choices=(('男', '男'), ('女', '女')))
    class_code = models.SmallIntegerField(verbose_name="班級", help_text='填寫數字代碼')
    seat_number = models.SmallIntegerField(verbose_name="座號", default=0)
    def __str__(self):
        return '' + self.name

    class Meta:
        ordering = ['class_code', 'seat_number']
        verbose_name_plural = '學生'


class Course_record(models.Model):
    course = models.ForeignKey(Course, on_delete=PROTECT, verbose_name="課程")
    student = models.ForeignKey(Students, on_delete=PROTECT, verbose_name='學生')
    course_order = models.SmallIntegerField(verbose_name='選課順序')
    allocation = models.BooleanField(verbose_name="已分配", default=False)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('student',)
        verbose_name_plural = '選課記錄'

class Group_record(models.Model):
    course = models.ForeignKey(Course, on_delete=PROTECT, verbose_name="課程")
    class_code = models.CharField(max_length=6, verbose_name="班級", default=0)
    student = models.ForeignKey(Students, on_delete=PROTECT, verbose_name="學生")
    timestamp = models.DateTimeField(default=datetime.now, verbose_name="登錄時間")
    course_order = models.SmallIntegerField(verbose_name='志願', default=0)

    # def __str__(self) -> str:self.course

    class Meta:
        verbose_name_plural = '志願分組'
        ordering = ('student', )