import json
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from utils.permissions import IsOwnerOrReadOnly

from django.contrib.auth import get_user_model
from .models import UserTrueAndFalse
from .serializers import UserTrueAndFalseSerializer2
User = get_user_model()

from Subject import settings
from utils.wechat_login import WxLogin


# Create your views here.


class WechatLoginView(APIView):
    """ 微信登录 """
    def post(self, request):
        data = request.data  # 获取微信数据
        code = data.get('code', '')
        if not code:
            return Response({'msg': '缺少code'}, status=status.HTTP_404_NOT_FOUND)

        # url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code" \
        #     .format(settings.APP_ID, settings.APP_KEY, code)
        # r = requests.get(url)
        # res = json.loads(r.text)
        # session_key = res['session_key'] if 'session_key' in res else None
        # res.pop('session_key', None)
        # 封装方法：微信返回的json数据
        wx = WxLogin()
        res = wx.getUserInfo(code)

        openid = res['openid'] if 'openid' in res else None
        if not openid:
            return Response({'message': '微信调用失败'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # 判断用户是否第一次登录
        try:
            user = User.objects.get(openid=openid)
        except Exception:
            # 微信用户第一次登陆,新建用户

            # username = request.data.get('nickname')
            # sex = request.data.get('sex')

            # 微信传递过来的openid，储存到数据库。
            # 微信再次请求，如果有openid就不新建，直接返回token给微信登录
            user = User.objects.create(username=openid,openid=openid)
            user.set_password(openid)
            user.save()

        # token
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        resp_data = {
            "user_id": user.id,
            "username": user.username,
            "token": token,
        }

        return Response(resp_data,status=status.HTTP_201_CREATED)


class UserTrueAndFalseView(mixins.ListModelMixin,GenericViewSet):

    serializer_class = UserTrueAndFalseSerializer2
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        return UserTrueAndFalse.objects.filter(user=self.request.user)