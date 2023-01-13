# -*- coding:UTF-8 -*-
import requests
import time
from bs4 import BeautifulSoup
import json

def get_info():
    url = "https://liunianbanxia.com/rabbit-and-fox-story.html#%s"%(2)
    try:
        response = requests.get(url=url)
        # r=response.content.decode('utf-8')
        soup = BeautifulSoup(response.text, "html.parser")  # 解析页面代码
        # print(soup)# soup.p.get('class')
        titles = soup.find_all("p")
        # print(titles)
        for title in titles:
            print(title.text)
        # url_info = soup.find_all("h1", class_="post-title")
        #
        # print(soup)
        # titlelist = []
        # for title in titles:
        #     titlelist.append(title.text.strip())
        # print(titlelist)

    except:
        pass

    def get_info():
        # url = "https://liunianbanxia.com/rabbit-and-fox-story.html#%s"%(2)
        try:
            response = requests.get(url=url)
            # r=response.content.decode('utf-8')
            soup = BeautifulSoup(response.text, "html.parser")  # 解析页面代码
            # print(soup)# soup.p.get('class')
            titles = soup.find_all("p")
            # print(titles)
            for title in titles:
                print(title.text)


        except:
            pass

    get_info()

# https://www.biquges.com/4_4218/2570142.html
# https://www.biquges.com/3_3468/2135500.html  <meta content="" name="keywords"/
#https://www.biquges.com/72_72645/index.html
def get_info1():
    for i in range(2570142, 24085908):
        url = "https://www.biquges.com/4_4218/%s.html"%(i)

        response = requests.get(url=url)
        # r=response.content.decode('utf-8')
        soup = BeautifulSoup(response.text, "html.parser")  # 解析页面代码
        title=soup.title.text
        txt=soup.find('div',id="content").text
        with open("D:\\code\\Python_code\\Water\Water\\a.txt", "a+",encoding="utf-8") as f:
            f.write(title+"\n"+txt.replace("\n", "")+"\n")  # 一次性读全部成一个字符串
        print(i)
        time.sleep(2)


def get_info2():

        url = "https://world.huanqiu.com/api/list?node=%22/e3pmh22ph/e3pmh2398%22,%22/e3pmh22ph/e3pmh26vv%22,%22/e3pmh22ph/e3pn6efsl%22,%22/e3pmh22ph/efp8fqe21%22&offset=40&limit=20"
        response = requests.get(url=url)
        r = json.loads(response.text)
        print(r)
        for i in range(len(r['list'])):
            print(r['list'][i]['source']['url'])
            #r ='https://content-static.cctvnews.cctv.com/snow-book/index.html?item_id=11628601626035573131'
            r = r['list'][i]['source']['url']
            print(r)
            response = requests.get(url=r)
            # print(response.text)
            # soup = BeautifulSoup(response.text, "html.parser")  # 解析页面代码
        # for i in range(len(soup["list"]))
        # title=soup.title.text
        # txt=soup.find('div',id="content").text
        # with open("D:\\code\\Python_code\\Water\Water\\a.txt", "a+",encoding="utf-8") as f:
        #     f.write(title+"\n"+txt.replace("\n", "")+"\n")  # 一次性读全部成一个字符串
        # print(i)
        # time.sleep(2)


if __name__ == '__main__':

    get_info2()


