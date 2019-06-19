from django.apps import AppConfig


class UserOperationConfig(AppConfig):
    name = 'user_operation'
    verbose_name = '操作'

    def ready(self):
        '''重载配置'''
        import user_operation.signals
