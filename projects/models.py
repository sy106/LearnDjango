from django.db import models

# Create your models here.
#1、每个应用下的数据库模型类，需要在当前应用下的models.py文件中定义
#2、一个数据库模型类相当于一个数据库表（table）
#3、一个数据库模型类，需要继承model或者model的子类
class Person(models.Model):
    """create Person class"""
    #4、定义的一个类属性，相当于数据库表中的一个字段，
    #5、默认会创建一个自动递增的ID主键
    #6、默认创建的数据库名为，应用名称小写_数据库模型类小写
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = '人类'
        verbose_name_plural = '人类'

class Project(models.Model):
    """project模型类"""
    #7,max_lenrth为最大长度
    #8，unique用于设置当前字段是否唯一，默认unique=False
    #9,verbose_name用于设置更人性化的设置
    #10.help_texty用于API文档里面的中文信息
    name = models.CharField(verbose_name='项目名称',max_length=200,unique=True,help_text='项目名称')
    leader = models.CharField(verbose_name='项目负责人', max_length=50, help_text='项目负责人')
    tester = models.CharField(verbose_name='测试人员', max_length=50, help_text='测试人员')
    programer = models.CharField(verbose_name='开发人员', max_length=50, help_text='开发人员')
    publish_app = models.CharField(verbose_name='发布应用', max_length=100, help_text='发布应用')
    #11.null设置数据库中此字段允许为空，blank用于设置前端可以不传递
    desc = models.TextField(verbose_name='简要描述', help_text='简要描述',blank=True,default='',null=True)
    #定义子类meta,用于设置当前数据模型的元数据信息
    class Meta:

        db_table='db_projects'
        # 会在ADMIN站点中，显示一个更人性化的表名
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.name





