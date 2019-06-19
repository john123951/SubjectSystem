# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/4/22 0022 13:08'


import xadmin
from .models import Subject,Category,Answer,RightWrongSub,ExamTime


class CategoryAdmin(object):
    ''' 类别 '''
    list_display = ["name", "category_type", "parent_category", "add_time"]


class SubjectAdmin(object):
    ''' 题目 '''
    list_display = ["name", "option_a", "option_b", "option_c","option_d", "category", "desc", "image", "fav_num", "add_time"]


class AnswerAdmin(object):
    ''' 答案 '''
    list_display = ["subject", "answer", "add_time","analysis"]


class RightWrongSubAdmin(object):
    ''' 对错 '''
    list_display = ["subject", "right_num", "wrong_num", "action", "add_time"]


class ExamTimeAdmin(object):
    ''' 考试时间 '''
    list_display = ["user",  "add_time"]


xadmin.site.register(Subject, SubjectAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Answer, AnswerAdmin)
xadmin.site.register(ExamTime, ExamTimeAdmin)
