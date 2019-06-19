# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/4/23 0023 12:53'


from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from topic.serializers import SubjectSerializer
from topic.models import Subject

from .models import UserFav,UserMessage


class UserFavSerializers(serializers.ModelSerializer):
    """
    用户收藏操作
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    subject = serializers.PrimaryKeyRelatedField(required=True, queryset=Subject.objects.all(), help_text="题目")

    class Meta:
        # 对构成唯一集合的字段,一个用户不能收藏两次同个商品
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'subject'),
                message="已经收藏"
            )
        ]
        model = UserFav
        fields = ("user", "subject", "id")  # 删除需要


class UserFavDetailSerializers(serializers.ModelSerializer):
    """
    个人信息收藏数据
    """
    # 设置当前登录用户，才能进行收藏
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        fields = ("user",  "subject", "id")  # 删除需要


class UserMessageSerializers(serializers.ModelSerializer):
    """
    用户留言
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')  # 返回api（add_time）给前端

    class Meta:
        model = UserMessage
        fields = ("user", "message_type", "subject", "message",  "add_time", "id")