from django.db import models


# Create your models here.

class Blog(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    path = models.CharField(max_length=2, verbose_name='路径')
    name = models.CharField(max_length=64, verbose_name='名称')

    title = models.CharField(max_length=128, verbose_name='标题')
    content = models.TextField(verbose_name='内容')

    is_deleted = models.BooleanField(default=False, verbose_name='已删除')

    def __str__(self):
        return self.name
