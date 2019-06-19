from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.
# User = get_user_model()

class UserProfile(AbstractUser):
    """ 用户扩展 """
    name = models.CharField(max_length=15,null=True,blank=True,verbose_name="姓名")  # 可以用手机号码和密码登录，不用名字
    image = models.ImageField(upload_to='image/%Y%m', default='image/default.png',max_length=100,verbose_name="头像",null=True,blank=True)
    birthday = models.DateField(null=True,blank=True,verbose_name="生日")
    gender = models.CharField(max_length=6,default='male', choices=(('male','男'), ('female','女')), verbose_name="性别")
    mobile = models.CharField(null=True,blank=True,max_length=11,verbose_name="手机号码")
    email = models.EmailField(max_length=100,null=True,blank=True,verbose_name="邮箱")
    openid = models.CharField(max_length=64,db_index=True, verbose_name='用户索引')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.username  # 父类AbstractUser原本的属性


#邮箱验证码
class EmailVerifyRecord(models.Model):
    send_choices = (
        ('provide','提供'),
        ('suggest ','建议'),
    )
    code = models.CharField(max_length=20,verbose_name="验证码",null=True,blank=True)
    email = models.EmailField(max_length=50,verbose_name="邮箱")
    #坑：send_choices > max_length：会出错
    send_type = models.CharField(choices=send_choices,max_length=20,verbose_name="验证码的类型")
    send_time = models.DateTimeField(default=datetime.now,verbose_name="发送时间")

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}{1}'.format(self.code,self.email)


#用户中心
class UserTrueAndFalse(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户")
    right_num = models.FloatField(default=0, verbose_name="正确率", null=True, blank=True)
    wrong_num = models.FloatField(default=0, verbose_name="错误率", null=True, blank=True)
    user_subject_sum_nums = models.IntegerField(default=0,verbose_name="答题总数",null=True,blank=True)

    class Meta:
        verbose_name = "用户正确与错误率"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}正确率 错误率{0}".format(self.right_num,self.wrong_num)