from django.contrib import admin
from projects.models import Project,Person
# from .models import Person,Project
# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    """
    定制后台管理类
    """
    #指定在修改（新增）中需要显示的字段
    fields = ('name','leader','tester','programer','publish_app')
    list_display = ['id','name','leader','tester']


admin.site.register(Project,ProjectsAdmin)
admin.site.register(Person)