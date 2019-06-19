"""Subject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.conf import settings #上传图片
from django.conf.urls.static import static #上传图片
from django.contrib import admin
from django.urls import path,include, re_path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls
from topic.views import SubjectViewSet,CategoryViewSet,RightWrongSubViewSet,AnswerViewSet,ExamTimeViewSet
from user_operation.views import UserFavViewSet,UserMessageViewSet
from users.views import WechatLoginView,UserTrueAndFalseView



router = DefaultRouter()  # 组合GenericViewSet方法，自动添加get、post、patch方法

# # 微信登录
# router.register('wx_login', WechatLoginView,base_name='wx_login')
# 答题
router.register('right_wrong', RightWrongSubViewSet,base_name='right_wrong')
# 答案
router.register('answer', AnswerViewSet,base_name='answer')
# 收藏
router.register('userfav', UserFavViewSet,base_name='userfav')
# 提供、留言
router.register('usermsg', UserMessageViewSet,base_name='usermsg')
# 考试时间和考试编号
router.register('exam', ExamTimeViewSet,base_name='exam'),
#类别
router.register("categorys",CategoryViewSet,base_name="categorys")
#用户对错率
router.register("usertf",UserTrueAndFalseView,base_name="sertf")


urlpatterns = [
    # 富文本编辑器url
    path('ueditor/', include('DjangoUeditor.urls')),
    path('xadmin/', xadmin.site.urls),
    # api显示登录按钮
    path('api-auth/', include('rest_framework.urls')),
    # 文档
    path('docs/', include_docs_urls(title='题目')),
    # 商品列表页
    re_path('^', include(router.urls)),
    # 随机题目
    path('subject/', SubjectViewSet.as_view(),name='subject'),
    # 登录
    path('login/', obtain_jwt_token),
    path('wx_login/', WechatLoginView.as_view(), name='wx_login'),
    # 类别
    # path('categorys/', CategoryViewSet.as_view(),name='categorys'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
