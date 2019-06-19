from datetime import datetime
from DjangoUeditor.models import UEditorField
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Category(models.Model):
    ''' 类别 '''
    CATEGORY_TYPE = (
        (1, "一级类别"),
        (2, "二级类别"),
    )
    name = models.CharField(max_length=100,verbose_name="类别名",help_text="类别名")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, default=1, verbose_name="类别级别", help_text="类别级别")
    image = models.ImageField(upload_to="category/images/", null=True, blank=True, verbose_name="图片")
    parent_category = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,verbose_name="当前类别的父级",related_name="sub_cat",help_text="当前类别的父级")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间",help_text="添加时间")

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Subject(models.Model):
    ''' 题目 '''
    name = models.CharField("题目", max_length=2000)
    option_a = models.CharField(max_length=100, verbose_name="a选项")
    option_b = models.CharField(max_length=100, verbose_name="b选项")
    option_c = models.CharField(max_length=100, verbose_name="c选项")
    option_d = models.CharField(max_length=100, verbose_name="d选项")
    category = models.ForeignKey(Category,  related_name='subject', on_delete=models.CASCADE, verbose_name="题目类别")
    desc = UEditorField(verbose_name=u"内容", imagePath="subject/images/", width=1000, height=300,
                              filePath="subject/files/", default='')
    image = models.ImageField(upload_to="subject/images/", null=True, blank=True, verbose_name="图片")
    fav_num = models.IntegerField("收藏数", default=0, null=True, blank=True, )
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '题目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Answer(models.Model):
    ''' 答案 '''
    subject = models.ForeignKey(Subject, related_name='answer', on_delete=models.CASCADE, verbose_name="题目答案")
    answer = models.CharField(verbose_name="答案", max_length=100)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)
    analysis = models.CharField(verbose_name="解析",default="",max_length=2000)

    class Meta:
        verbose_name = '答案'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.answer


class RightWrongSub(models.Model):
    ''' 对错题'''

    Action_TYPE = (
        ('1', "正确"),
        ('0', "错误"),
    )
    user = models.ForeignKey(User,default='', on_delete=models.CASCADE, verbose_name="用户")
    subject = models.ForeignKey(Subject, related_name='right_wrong', on_delete=models.CASCADE, verbose_name="题目")
    # right_num = models.IntegerField(default=0, verbose_name="正确率", null=True, blank=True)
    # wrong_num = models.IntegerField(default=0, verbose_name="错误率", null=True, blank=True)
    action = models.CharField(max_length=20, choices=Action_TYPE, default=1, verbose_name="对错类别", help_text="对错类别")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '题目对错'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class ExamTime(models.Model):
    exam_number = models.CharField(max_length=30,null=True,blank=True,verbose_name="考试编号")
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE, verbose_name="答题者")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '考试时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user



