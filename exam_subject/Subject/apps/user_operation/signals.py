# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/3/13 0013 19:35'
# 保存最后一刻，会执行信号量

from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import UserFav


@receiver(post_save, sender=UserFav)
def create_user_fav(sender, instance=None, created=False, **kwargs):
    if created:
        # 是否新建，因为update也会执行post_save
        subject = instance.subject
        subject.fav_num += 1
        subject.save()


# 收藏数 - 1
@receiver(post_delete, sender=UserFav)
def create_user_fav(sender, instance=None, created=False, **kwargs):
    subject = instance.subject
    subject.fav_num -= 1
    subject.save()
