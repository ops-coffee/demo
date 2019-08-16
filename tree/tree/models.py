from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='名称')
    parent = models.ForeignKey('self', on_delete=models.PROTECT, db_constraint=False,
                               null=True, blank=True, verbose_name='父部门')

    def __str__(self):
        return self.name
