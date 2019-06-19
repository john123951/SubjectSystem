# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/4/22 0022 19:09'

from datetime import datetime
from datetime import timedelta
from rest_framework import serializers
from .models import Category,Subject,Answer,RightWrongSub,ExamTime


class CategorySerializer2(serializers.ModelSerializer):
    """
    二级分类
    """
    count = serializers.SerializerMethodField()  # 新增字段

    def get_count(self, obj):
        '''
        处理count
        返回二级分类数量
        obj：当前类型
         '''
        return Subject.objects.filter(category=obj).count()

    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    一级分类：
        many=True：列表必须加
    """

    sub_cat = CategorySerializer2(many=True)
    count = serializers.SerializerMethodField()  # 新增字段

    def get_count(self, obj):
        '''
        处理count
        返回具体类型的题目数量
        obj：当前类型
         '''
        return Category.objects.filter(category_type=2).count()

    class Meta:
        model = Category
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    ''' 获取单个或者多个答案  '''

    class Meta:
        model = Answer
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    """
    题目
    """
    category = CategorySerializer()
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')  # 返回api（add_time）给前端
    answer = AnswerSerializer(many=True)  # Subject.answer：获取当前题目的答案

    class Meta:
        model = Subject
        fields = '__all__'


class RightWrongSubSerializer(serializers.ModelSerializer):
    """
    对错
    """
    # # 当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    # subjece = SubjectSerializer(many=False)
    # answer = serializers.CharField(help_text="请填写答案")
    # subject = serializers.PrimaryKeyRelatedField(required=True, queryset=Subject.objects.all(), help_text="题目")
    # 只读不写
    # right_num = serializers.CharField(read_only=True)
    # wrong_num = serializers.CharField(read_only=True)
    #
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')


    # def validate(self, attrs):
    #     '''
    #     删除数据库没有的字段
    #     '''
    #     del attrs["answer"]  # 删除自定义的code,不需要传递给User
    #     return attrs

    class Meta:
        model = RightWrongSub
        fields = "__all__"


class RightWrongSubDetailSerializer(serializers.ModelSerializer):
    """
    个人中心答题列表
    """
    # 当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    subject = SubjectSerializer()  # 一个题目对应一个答题

    class Meta:
        model = RightWrongSub
        fields = '__all__'


class ExamTimeSerializer(serializers.ModelSerializer):

    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    # 当前用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    user_true_nums = serializers.IntegerField(help_text="对的数量")
    user_false_nums = serializers.IntegerField(help_text="错的数量")

    times =  serializers.SerializerMethodField()


    def validate_add_time(self, add_time):
        '''
        考试时间
        '''
        # 前30分钟
        thirty_minuter_age = datetime.now() - timedelta(hours=0, minutes=30, seconds=0)
        if RightWrongSub.objects.filter(add_time__lte=thirty_minuter_age):
            raise serializers.ValidationError("超过30分钟，考试结束")
        return add_time

    class Meta:
        model = ExamTime
        fields = '__all__'


class ExamTimeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamTime
        fields = '__all__'