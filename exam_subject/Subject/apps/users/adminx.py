# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/4/22 0022 13:08'


import xadmin
from xadmin import views
from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ('code', 'email', 'send_type', 'send_time')
    # 搜索的字段，不要添加时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']
    model_icon = 'fas fa-at'


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


# 配置xadmin
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True  # 调用更多主题


class GlobalSettings(object):
    #修改左上角的title
    site_title = '刷题佬后台管理界面'
    #修改footer
    site_footer = '刷题佬的公司'
    #收起菜单
    menu_style = 'accordion'


# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSettings)#views.(点)
# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)