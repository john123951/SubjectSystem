#__file__ : email_send.py 
__author__: '田敏伦'
__date__: '2018/12/12 0012 20:32'

from django.core.mail import send_mail
from users.models import EmailVerifyRecord
from Subject.settings import EMAIL_FROM,MYEMAIL


def send_register_email(email_title, email_body, send_type='provide'):
    """
    :param email: 用户的邮箱
    :param send_type: 发送的类型
    :return:
    """
    email_record = EmailVerifyRecord()#实例化
    email_record.email = MYEMAIL #views（用户输入）传递过来的邮箱
    email_record.send_type = send_type #默认发送类型为注册(register)
    email_record.save() #code先保存在数据库

    #判断发送类型
    if send_type == "provide":
        # 提供
        email_title = "客户提供题目：（{}）".format(email_title)
        email_body = email_body
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [MYEMAIL])  # 会返回一个值（true / false）
        #如果邮箱发送出去了
        if send_status:
            pass

    elif send_type == "suggest":
        # 建议
        email_title = "客户留言及建议：（）".format(email_title)
        email_body = email_body
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [MYEMAIL])

        if send_status:
            pass
