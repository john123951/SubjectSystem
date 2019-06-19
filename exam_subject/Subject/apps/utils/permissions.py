# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/3/14 0014 23:06'

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # obj：模型
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user  # 在此修改owner为user