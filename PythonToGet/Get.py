# -*- coding:UTF-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import time
import os

# 调用百度语音合成
from aip import AipSpeech
# 调用百度语言处理
from aip import AipNlp


def GetBaiduNews():
    #理解文章内容
    """ 你的 APPID AK SK """
    APP_ID = '10350986'
    API_KEY = 'iMANyu1j6gTQCkgG9xCGAOd5'
    SECRET_KEY = '9dbb7a3166312c7eba296fa4ec72c19d'
    # client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)    

    if __name__ == '__main__':

        resp=urlopen('http://news.baidu.com/guoji')
        soup=BeautifulSoup(resp,'html.parser')

        # target = 'http://news.baidu.com/guoji'
        # req = requests.get(url=target)
        # html = req.text

        # bf = BeautifulSoup(html,'html.parser')
 
        title = soup.find_all('a',class_='title')
        # client =AipNlp(APP_ID, API_KEY, SECRET_KEY)
        result  = client.synthesis("现在给您播报今日即时新闻", 'zh', 1, {
            'vol': 10,
            'spd': 4,

        })

        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            # os.path.join(os.path.abspath('.'),'News_'+time.strftime('%Y-%m-%d',time.localtime()))
            if(os.path.exists(os.path.abspath('.')+'/News_'+time.strftime('%Y-%m-%d',time.localtime()))== False):
                os.rmdir(os.path.abspath('.')+'/News_'+time.strftime('%Y-%m-%d',time.localtime()))
            # os.mkdir(os.path.abspath('.')+'/News_'+time.strftime('%Y-%m-%d',time.localtime()))
            with open('News_'+time.strftime('%Y-%m-%d',time.localtime())+'/News_'+ "0" +"_" + time.strftime('%Y-%m-%d',time.localtime()) + ".mp3", 'wb') as f:
                f.write(result)
        i = 1
        for OutTexts in title:
            print(OutTexts.string)
            # EndTexts = OutTexts.string + "。"

        # client =AipNlp(APP_ID, API_KEY, SECRET_KEY)
            result  = client.synthesis(OutTexts.string+"。", 'zh', 1, {
                'vol': 10,
                'spd': 4,
            })
            # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
            if not isinstance(result, dict):                
                with open('News_'+time.strftime('%Y-%m-%d',time.localtime())+'/News_'+ str(i) +"_" + time.strftime('%Y-%m-%d',time.localtime()) + ".mp3", 'wb') as f:
                    f.write(result)
            i+=1    
        

GetBaiduNews()
        
    
    # for OutTexts in texts:
    #     print(OutTexts.text.replace('\xa0'*16,'\n\n'))
    #     # 写入文件 
    #     with open("E:/python/"+"News_"+time.strftime('%Y-%m-%d',time.localtime())+".txt", "a") as f: 
    #         f.write("%s\n" % (OutTexts.text.replace('\xa0'*16,'\n\n')))
    #         f.write("====================================================\n")




def GetWeather():
    if __name__ == '__main__':
        # target = 'http://www.weather.com.cn/weather/101260515.shtml'
        # req = requests.get(url=target)
        # html = req.text
        # print(html)
        #bfs = BeautifulSoup(html)

        resp=urlopen('http://www.weather.com.cn/weather/101260515.shtml')
        soup=BeautifulSoup(resp,'html.parser')
        tagToday=soup.find('p',class_="tem")  #第一个包含class="tem"的p标签即为存放今天天气数据的标签
        try:
            temperatureHigh=tagToday.span.string  #有时候这个最高温度是不显示的，此时利用第二天的最高温度代替。
        except AttributeError as e:
            temperatureHigh=tagToday.find_next('p',class_="tem").span.string  #获取第二天的最高温度代替

        temperatureLow=tagToday.i.string  #获取最低温度
        weather=soup.find('p',class_="wea").string #获取天气



        #tagToday = bfs.find('p',class_='tem')
        


        # tem_lowest = tems[0]
        # tem_max = tems[1]

        # if int(tems[0]) < int(tems [1]):
        #     tem_lowest = tems[0]
        #     tem_max = tems[1]
        # else :
        #     tem_lowest = tems[1]
        #     tem_max = tems[0]

        # weather_text = bf.find_all('p',class_='wea')
        
        #print(tems)
        with open("E:/python/"+"Weather_"+time.strftime('%Y-%m-%d',time.localtime())+".txt", "a") as f: 
            f.write("黔东南锦屏县气温：\n")
            f.write("最高温度：%s\n 最低温度：%s 度\n 天气情况：%s\n " % (temperatureHigh, temperatureLow,weather))
            f.write("=======================================")


        """ 你的 APPID AK SK """
        APP_ID = '10350986'
        API_KEY = 'iMANyu1j6gTQCkgG9xCGAOd5'
        SECRET_KEY = '9dbb7a3166312c7eba296fa4ec72c19d '

        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        # client =AipNlp(APP_ID, API_KEY, SECRET_KEY)
        result  = client.synthesis("黔东南锦屏县"+time.strftime('%Y-%m-%d',time.localtime())+"天气情况："+ "今天天气:"+weather+"。" + "最高气温:" +temperatureHigh +"。"+ "最低气温:"+temperatureLow, 'zh', 1, {
            'vol': 10,
            'spd': 4,

        })
        # print(time.strftime('%Y年%m月%d日',time.localtime()))

        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            if(os.path.exists(os.path.abspath('.')+'/Weathers_'+time.strftime('%Y-%m-%d',time.localtime()))== False):
                os.rmdir(os.path.abspath('.')+'/Weathers_'+time.strftime('%Y-%m-%d',time.localtime()))
            
            with open('Weathers_'+time.strftime('%Y-%m-%d',time.localtime())+'/weather_'+time.strftime('%Y-%m-%d',time.localtime())+'.mp3', 'wb') as f:
                f.write(result)


GetWeather()
            
