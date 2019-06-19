import datetime
from datetime import datetime
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend  # 过滤
from rest_framework import filters  # 搜索
from rest_framework import status
from rest_framework import serializers

from .models import Subject,Category,Answer,RightWrongSub, ExamTime
from .serializers import SubjectSerializer,CategorySerializer,AnswerSerializer,RightWrongSubSerializer,RightWrongSubDetailSerializer,ExamTimeDetailSerializer,ExamTimeSerializer
from users.models import UserTrueAndFalse
from utils.permissions import IsOwnerOrReadOnly
# Create your views here.


class SubjectViewSet(APIView):
    """
    题目
    list:
        获取题目数据
    retrieve:
        单个题目数据
    """
    # def get(self, request):
    #     subject = Subject.objects.all()
    #     subject_list = SubjectSerializer(subject, many=True)
    #
    #     return Response(subject_list.data)

    def post(self, request):
        ''' 动态传递随机题目 '''
        # 获取值
        sub_category = request.data.get('sub_category', '')  # 获取类型
        sub_nums = int(request.data.get("sub_nums", 0))   # 获取数量
        if sub_category and sub_nums:
            # Subject对应的外键是id（category=id），如果要找name：category__name='Java'
            subjects = Subject.objects.filter(category__name=sub_category,category_type=2)

            subject = subjects.order_by('?')[: sub_nums]  # 随机返回题目
            subject_list = SubjectSerializer(subject, many=True)  # 系列化
            return Response(subject_list.data)  # 返回数据
        else:
            return Response({'msg': '错误请求'},status=status.HTTP_404_NOT_FOUND)


# class CategoryViewSet(APIView):
#     """
#     类别
#     list:
#         获取所有类别数据
#     retrieve:
#         单个类别数据
#     """
#     def get(self, request):
#         category = Category.objects.filter(category_type=1)
#         category_list = CategorySerializer(category, many=True)
#         return Response(category_list.data)

class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    """
    类别
    list:
        获取所有类别数据
    retrieve:
        单个类别数据
    """
    queryset = Category.objects.filter(category_type=1)
    serializer_class = CategorySerializer

class AnswerViewSet(mixins.RetrieveModelMixin,GenericViewSet):
    """
    答案
    list:
        获取答完题的数据
    create:
        创建答题试卷
    """
    queryset = Answer.objects.all()  # 最初先系列化一级分类
    serializer_class = AnswerSerializer  # 系列化
    lookup_field = "subject_id"  # 根据题目id查询答案


class RightWrongSubViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    """
    创建答题
    list:
        获取答完题的数据
    create:
        创建答题试卷
    retrieve:
        一个题目对应一个答题
    """
    # 验证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    lookup_field = "subject_id"
    #排序过滤器
    search_fields = ("add_time",)

    def get_serializer_class(self):
        ''' 动态系列化 '''
        if self.action == 'list':
            # 详情页，需要商品数据
            return RightWrongSubDetailSerializer
        # 订单的列表、创建、删除
        return RightWrongSubSerializer

    # def create(self, request, *args, **kwargs):
    #     # astrict = int(request.POST.get("astrict", ""))  # 动态获取限制答题数
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     # 手动创建实例
    #
    #     subject = serializer.validated_data["subject"]  # 题目
    #     # get_answer = str(serializer.validated_data["answer"])
    #     # answers = subject.answer.all()  # 所有答案
    #
    #     # if RightWrongSub.objects.filter(add_time=datetime.date.today(), user=request.user).count() > astrict:
    #     #     raise serializer.ValidationError("你今天答题数以满")
    #
    #     # for answer in answers:
    #     #     # 遍历所有答案，可能是多选题
    #     #     if get_answer == str(answer):
    #     #         # 答案正确
    #     #         right_wrong = RightWrongSub()
    #     #         right_wrong.user = request.user
    #     #         right_wrong.action = "正确"
    #     #         right_wrong.right_num += 1
    #     #         right_wrong.subject = subject
    #     #         right_wrong.save()
    #     #         raise serializers.ValidationError('答对')
    #     #     elif get_answer != answer:
    #     #         # 答案错误
    #     #         right_wrong = RightWrongSub()
    #     #         right_wrong.user = request.user
    #     #         right_wrong.action = "错误"
    #     #         right_wrong.wrong_num += 1
    #     #         right_wrong.subject = subject
    #     #         right_wrong.save()
    #     #         raise serializers.ValidationError('打错，参考答案：%s' % answer)
    #     #     else:
    #     #         raise serializers.ValidationError('答错了')
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        #控制列表输出
        return RightWrongSub.objects.filter(user=self.request.user)

        # year = self.request.query_params.get('year', None)
        # month = self.request.query_params.get('month', None)
        # if year and month:
        #     return RightWrongSub.objects.filter(add_time__year=year).filter(add_time__month=month)




class ExamTimeViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,GenericViewSet):

    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def create(self, request, *args, **kwargs):
        # astrict = int(request.POST.get("astrict", ""))  # 动态获取限制答题数
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        user_true_nums = int(request.POST.get("user_true_nums",0))
        user_false_nums = int(request.POST.get("user_false_nums",0))

        sum =  int(user_true_nums + user_false_nums)

        try:
            user_true_false= UserTrueAndFalse.objects.get(user=self.request.user)
            sum +=user_true_false.user_subject_sum_nums

        except:
            user_true_false = UserTrueAndFalse()
            user_true_false.user = self.request.user

        user_true_false.right_num = float(sum/user_true_nums)
        user_true_false.wrong_num = float(sum/user_false_nums)
        user_true_false.user_subject_sum_nums = sum
        user_true_false.save()


        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return ExamTime.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        ''' 动态系列化 '''
        if self.action == 'list':
            return ExamTimeDetailSerializer
        return ExamTimeSerializer

