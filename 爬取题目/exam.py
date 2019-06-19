# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2019\4\22 0022 10:21$'

import io
import time
import re
import requests
import json
from lxml import etree





def get_exam_url():

    header = {
        'User - Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    url = "https://www.examcoo.com/paperlist/index/k/661/p/1"
    html = requests.get(url=url,headers=header)

    url_etree  = etree.HTML(html.text)

    url_list = url_etree.xpath("//div[@class='table-responsive']/table/tbody/tr/td[7]/a[1]/@href")
    # print(url_list[1:3])

    return url_list[5:]

#获取解析
def get_analysis(subjet_id,sdtId,pid,tokenpid):
    header = {
        'User - Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    data = {
        "id": subjet_id,
        "sdtId": sdtId,
        "pid": pid,
        "p": 1,
        "l": 0,
        "msgid": 0,
        "cmid": 0,
        "tid": 0,
        "verifydtid": 0,
        "tokenpid": tokenpid
    }

    html = requests.post(url="https://www.examcoo.com/editor/comment/index",data=data,headers=header)
    try:
        print(html.text)

        analysis_html = html.text

        matchObj = re.match('.*?试题解析：.*?<div>(.*?)</div>.*?<div.*?>', analysis_html, re.S)

        if matchObj:
            analysis = matchObj.group(1)
            print(analysis)
            return analysis

        else:
            return ""

    except:
        pass


def get_exam_subject(url_list):

    header = {
        'User - Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }

    for url in url_list:

        time.sleep(5)


        url = 'https://www.examcoo.com' + url
        print(url)


        html = requests.get(url=url,headers=header)


        url_ertee = etree.HTML(html.text)


        exam_subject_list  = url_ertee.xpath('//div[contains(@class,"singleContainer") and contains(@class,"questionArea")]')[:-20]


        # 爬取题目的token值
        str_token = url_ertee.xpath("/html/body/script[1]/text()")[0].strip()
        # print(str_token)
        matchObj = re.match('.*?pid.*?"(.*)";var.*?tokenpid.*?"(.*)";.*?anchorId', str_token, re.S)

        if matchObj:
            # print(matchObj.group(1))
            pid = matchObj.group(1)
            tokenpid = matchObj.group(2)


        for exam_subject in exam_subject_list:

            subject_title = exam_subject.xpath('div[1]/div[2]/text()')

            subject_id = exam_subject.xpath("@id")[0]
            data_anchor = exam_subject.xpath("@data-anchor")[0]
            print(subject_id,data_anchor)

            analysis = get_analysis(data_anchor,subject_id,pid,tokenpid)

            if len(subject_title) > 0 :
                    subject_title = '\n'.join(subject_title)

            else:
                subject_title = subject_title[0]
            # print(subject_title)

            try:
                subject_choice_A = exam_subject.xpath("div[2]/div[1]/div[2]/text()")[0]
                subject_choice_B = exam_subject.xpath("div[2]/div[2]/div[2]/text()")[0]
                subject_choice_C = exam_subject.xpath("div[2]/div[3]/div[2]/text()")[0]
                subject_choice_D = exam_subject.xpath("div[2]/div[4]/div[2]/text()")[0]
                # print(subject_choice_D)

                subject_answer = exam_subject.xpath("div[2]/div/div[1]/label/div[contains(@class,'dijitReset') and contains(@class,'dijitRadioCheckedDisabled')]/following-sibling::div/text()")


                yield {
                    "subject_title":subject_title,
                    "subject_choice_A":subject_choice_A,
                    "subject_choice_B":subject_choice_B,
                    "subject_choice_C":subject_choice_C,
                    "subject_choice_D":subject_choice_D,
                    "subject_answer" :subject_answer[0],
                    "analysis":analysis
                }
            except:
                pass



def write_json(json_dict):
    print(json_dict)
    jsonFile = io.open("subject_list_cc.json", 'a+', encoding='utf8')
    jsonFile.write(json.dumps(json_dict, ensure_ascii=False))
    jsonFile.flush()
    jsonFile.close()




def main():
    write_json_dict = []
    for i in get_exam_subject(get_exam_url()):
        write_json_dict.append(i)

    write_json(write_json_dict)






if __name__ == '__main__':
    main()
