# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/4/23 0023 12:53'


import xadmin
from .models import UserFav, UserMessage


class UserFavAdmin(object):
    ''' 用户收藏 '''
    list_display = ["user", "subject", "add_time"]


class UserMessageAdmin(object):
    ''' 用户留言 '''
    list_display = ["user", "message_type", "subject", "message", "add_time"]


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
