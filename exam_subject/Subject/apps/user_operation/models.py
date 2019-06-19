from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from topic.models import Subject

User = get_user_model()
# Create your models here.


class UserFav(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="题目",help_text="题目id")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '题目收藏'
        verbose_name_plural = verbose_name
        # 设置user不能有同一时间收藏同个goods（不能有相同的记录），如果错误数据库会抛出异常
        unique_together = ("user", "subject")

    def __str__(self):
        return "{0}收藏{1}".format(self.user.username,self.subject)


class UserMessage(models.Model):
    MESSAGE_CHOICES = (
        (1,"提供"),
        (2,"留言"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    message_type = models.CharField(max_length=30,choices=MESSAGE_CHOICES,default=1,verbose_name="留言类型")
    subject = models.CharField(max_length=100,default="",verbose_name="主题")
    message = models.TextField(default="",verbose_name="留言内容",help_text="留言内容")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = '用户留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject