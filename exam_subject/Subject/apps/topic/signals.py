# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/3/13 0013 19:35'
# 保存最后一刻，会执行信号量

from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import RightWrongSub
from users.models import UserTrueAndFalse


# 只有post_save（create, update）和post_delete(destroy)才会执行信号量
# created： post_save（create, update）才执行
@receiver(sender=RightWrongSub,post_save)
def create_user_fav(sender, instance=None, created=False, **kwargs):
    '''
    对错题数量 + 1
    :param sender:模型类
    :param instance:保存的实际实例（对象）
    :param created: 只有新增和修改的时候created=True；其他操作都是created=False
    '''
    if created:
        # 是否新建，因为update也会执行post_save
        if instance.action == '1':
            user_true_false = UserTrueAndFalse()
            user_true_false.right_num += 1
            user_true_false.save()
            instance.save()
        elif instance.action == '0':
            user_true_false = UserTrueAndFalse()
            user_true_false.wrong_num += 1
            user_true_false.save()
            instance.save()

