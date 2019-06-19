from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers

from .serializers import UserFavSerializers, UserFavDetailSerializers, UserMessageSerializers
from .models import UserFav, UserMessage

from utils.permissions import IsOwnerOrReadOnly
from utils.email_send import send_register_email
# Create your views here.


class UserFavViewSet(ModelViewSet):
    """
    用户收藏操作
    create:
        收藏
    delete:
        取消收藏
    list:
        个人中心的收藏列表
    retrieve:
        通过url的参数（goods_id）来判断某个商品是否收藏
    """
    # 验证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # 根据题目id查找，收藏
    lookup_field = 'subject_id'

    def get_serializer_class(self):
        if self.action == 'list':
            return UserFavDetailSerializers
        elif self.action == 'create':
            # 操作
            return UserFavSerializers
        return UserFavSerializers

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        '''
        收藏数 + 1
        '''
        instance = serializer.save()
        subject = instance.subject
        subject.fav_num += 1
        subject.save()

    def perform_destroy(self, instance):
        '''
        收藏数 - 1
        '''
        instance = instance.delete()
        subject = instance.subject
        subject.fav_num -= 1
        subject.save()


class UserMessageViewSet(ModelViewSet):
    """
       用户留言操作
       create:
           添加留言
       delete:
           取消留言
       list:
           个人中心的留言列表
        update:
            修改留言
       """
    # 验证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    serializer_class = UserMessageSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            message_type = str(serializer.validated_data["message_type"])
            subject = serializer.validated_data["subject"]

            message = serializer.validated_data["message"]
            bad_language = ['妈','操','叼','做爱','屎','扑','街','死','拜拜']

            for bad in bad_language:
                if bad in message:
                    message = message.replace(bad, "*")
        except Exception as e:
            raise serializers.ValidationError('输入错误')

        # 保存数据，发送邮箱
        if message_type == '1':
            # 提供
            user_message = UserMessage()
            user_message.user = request.user
            user_message.message_type = '提供'
            user_message.subject = subject   # 主题
            user_message.message = message
            user_message.save()
            # 发送邮箱
            send_register_email(subject, message, 'provide')

        elif message_type == '2':
            # 留言
            user_message = UserMessage()
            user_message.user = request.user
            user_message.message_type = '留言'
            user_message.subject = subject   # 主题
            user_message.message = message
            user_message.save()
            # 发送邮箱
            send_register_email(subject, message, 'suggest')

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return UserMessage.objects.filter(user=self.request.user)
