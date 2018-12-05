from django.db import models


# Create your models here.
class Table(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    host = models.GenericIPAddressField(verbose_name='主机地址')
    port = models.IntegerField(default=3306, verbose_name='主机端口')

    username = models.CharField(max_length=64, verbose_name='用户名')
    password = models.CharField(max_length=512, verbose_name='密码')

    owner = models.CharField(max_length=32, verbose_name='需求方')
    contact = models.CharField(max_length=128, verbose_name='联系人')

    notes = models.TextField(null=True, verbose_name='备注')

    def __str__(self):
        return self.host

    class Meta:
        default_permissions = ()

        permissions = (
            ("select_table", "查看密码表"),
            ("change_table", "修改密码表"),
            ("decode_password", "解密加密密码")
        )
