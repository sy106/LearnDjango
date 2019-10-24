#-*- coding:utf-8 -*-
# @Time     : 2019/10/24 16:49
# @Author   : shenyuan
# @Email    : shenyuan@suray.cn
# @File     : pagination.PY
from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    page_query_param = 'p'
    page_size = 2#默认情况下，每一页显示为2条
    page_size_query_param = 's'
    max_page_size = 50#指定前端能分页的最大page_size
