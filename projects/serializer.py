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
def is_unique_project_name(name):
    if '项目' not in name:
        raise serializers.ValidationError('项目名称中必须包含“项目”关键字')

#1.继承Serializer类或者子类
class ProjectsSerialzer(serializers.Serializer):
    """
    创建项目序列化器类
    需要哪些字段，就在序列化器里定义哪些字段
    """
    #1. 序列话器中定义的属性字段往往与模型字段一一对应
    #2.lable选项相当于vervbose_name,help_text
    #3.定义的序列化器字段，默认既可以进行序列化输出，也可以进行反序列化输入
    #4.read_only=True,指定该字段只能进行序列化输出，
    #5.write_only=True,指定该字段只能进行反序列化输入，但不进行序列化输出
    ## 需要输出哪些字段就在序列化器中定义哪些字段
    id = serializers.IntegerField(label='ID')
    #write_only=True指定该字段只进行序列化输入，不进行序列化输出
    name = serializers.CharField(label='项目名称',max_length=200,help_text='项目名称',
                                 validators=[UniqueValidator(queryset=Project.objects.all(),message='项目名称不能重复'),is_unique_project_name],
                                 error_messages={'max_length':'长度不能超过200字节'})
    leader = serializers.CharField(label='负责人', min_length=6,max_length=50, help_text='负责人',
                                   error_messages={'max_length':'长度不能超过200字节',
                                                   'min_length':'长度不能少于6个字节'})
    tester = serializers.CharField(label='测试人员', max_length=50, help_text='测试人员')
    programer = serializers.CharField(label='开发人员',max_length=50,help_text='开发人员')
    publish_app = serializers.CharField(label='发布应用', max_length=100, help_text='发布应用')
    desc = serializers.CharField(label='简要描述', help_text='简要描述', allow_blank=True, allow_null=True)

#单字段的校验
#字段效验器的顺序
#字段定义时的限制（包含validators列表条目从左到右进行校验）-》单字段的校验（validate_字段名）-》多字段联合校验（validate）
#单字段的校验器，validate_字段名
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

    def create(self, validated_data):

        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.leader = validated_data['leader']
        instance.programer = validated_data['programer']
        instance.publish_app = validated_data['publish_app']
        instance.desc = validated_data['desc']
        instance.save()
        return instance



class ProjectsModelSerialzer(serializers.ModelSerializer):

    class Meta:
        #1.指定参考哪个模型类来创建
        model = Project
        #2.指定为模型类的哪些字段，来生成序列化器
        # fields = "__all__"
        fields = ('id','name','leader','tester','programer','publish_app')
        # exclude= ('publish_app','desc')#排除掉哪些
        # read_only_fields =('leader','tester')
        # extra_kwargs={
        #     'leader':{
        #
        #         'error_message':{'max_length':'最大长度不超过50字节'}
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