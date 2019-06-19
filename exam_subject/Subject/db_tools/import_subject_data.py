# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/4/22 0022 14:25'


# 导入goods的数据
import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Subject.settings")

import django
django.setup()

from db_tools.data.subject_list import data
from topic.models import Subject,Answer,Category


def get_subject():
  for i in data:
    print(i)
    subject = Subject()
    subject.name = i['subject_title'] if i['subject_title'] is not None else ""
    subject.option_a = i['subject_choice_A'] if i['subject_choice_A'] is not None else ""
    subject.option_b = i['subject_choice_B'] if i['subject_choice_B'] is not None else ""
    subject.option_c = i['subject_choice_C'] if i['subject_choice_C'] is not None else ""
    subject.option_d = i['subject_choice_D'] if i['subject_choice_D'] is not None else ""
    type = Category.objects.filter(name="Java")
    if type:
      subject.category = type[0]
    subject.save()

    answer = Answer()
    answer.subject = subject
    answer.answer = i['subject_answer'] if i['subject_answer']  is not None else ""
    answer.analysis = i["analysis"] if i["analysis"] is not None else "暂无解析"
    answer.save()


def main():
  get_subject()


if __name__ == '__main__':
  main()







