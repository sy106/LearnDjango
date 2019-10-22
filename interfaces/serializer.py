#-*- coding:utf-8 -*-
# @Time     : 2019/10/18 10:52
# @Author   : shenyuan
# @Email    : shenyuan@suray.cn
# @File     : serializer.PY


from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from projects.models import Project
from rest_framework import serializers

#创建自定义校验器
#1.第一个参数为字段的值
from projects.serializer import is_unique_project_name,ProjectsSerialzer
from interfaces.models import Interfaces


class InterfaceModelSerialzer(serializers.ModelSerializer):
    #1.数据库模型中的外键字段，默认会生成PrimaryKeyRelatedField序列化器字段
    #序列化输出的值，为外键ID值

    #2.StringRelatedField,此字段将被序列化为关联对象字符串表达形式（即__str__方法返回值）
    # project =serializers.StringRelatedField(label='所属项目')

    #3.SlugRelatedField,此字段将被序列化为关联对象的指定字段的数据
    # project = serializers.SlugRelatedField(slug_field='tester',read_only=True)
    # 4.SlugRelatedField,此字段将被序列化为关联对象的指定字段的数据
    # project = ProjectsSerialzer(label='所属项目',read_only=True)

    #父表中默认不会生成从表的关联字段，可以手动添加，字段名默认为，指标模型类名小写_set
    interfaces_set = serializers.StringRelatedField(many=True)
    class Meta:

        #1.指定参考哪个模型类来创建
        model = Interfaces
        #2.指定为模型类的哪些字段，来生成序列化器
        fields = "__all__"
        # fields = ('id','name','leader','tester','programer','publish_app')
        # exclude= ('publish_app','desc')#排除掉哪些
        # read_only_fields =('leader','tester')
        # extra_kwargs={
        #     'leader':{
        #         'write_only':True,
        #         'error_message':{'max_length':'最大长度不超过50字节',}
        #     }
        # }
    def validate_name(self,value):
        if not value.endswith('项目'):
            raise serializers.ValidationError('项目必须以“项目”结尾')
        return value #当校验成功后，一定要返回value

    def validate(self,attrs):
        """
        多字段联合校验
        :param self:
        :param attrs:
        :return:
        """
        if 'icon' not in attrs['tester'] and 'icon' not in attrs['leader']:
            raise serializers.ValidationError('"icon"必须是项目负责人或项目测试人员')
        return attrs