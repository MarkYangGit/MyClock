#-*- coding:UTF-8 -*-
import requests
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import os
import wechatsogou

# 调用百度语音合成
from aip import AipSpeech
# 调用百度语言处理
from aip import AipNlp

# 设置超时
ws_api = wechatsogou.WechatSogouAPI(timeout=0.1)

def GetUrl():
    urlnext = ws_api.search_article('早啊！新闻来了'+time.strftime('%Y.%m.%d',time.localtime()))

    urlgo = urlnext[0]
    print(urlgo['article']['url'])
    return urlgo['article']['url']

def GetArticle():
    url = GetUrl()
    #初始化SDK
    """ 你的 APPID AK SK """
    APP_ID = '10350986'
    API_KEY = 'iMANyu1j6gTQCkgG9xCGAOd5'
    SECRET_KEY = '9dbb7a3166312c7eba296fa4ec72c19d'
    # client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # client =AipNlp(APP_ID, API_KEY, SECRET_KEY)
    result  = client.synthesis("现在给您播报今日即时新闻", 'zh', 1, {
        'vol': 10,
        'spd': 4,

    })
    # os.path.join(os.path.abspath('.'),'New_'+time.strftime('%Y-%m-%d',time.localtime()))
    if(os.path.exists('News_'+time.strftime('%Y-%m-%d',time.localtime()))== False):
        os.mkdir('News_'+time.strftime('%Y-%m-%d',time.localtime()))
    # os.mkdir('News_'+time.strftime('%Y-%m-%d',time.localtime()))
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        
        with open('News_'+time.strftime('%Y-%m-%d',time.localtime())+'/News_'+ "0" +"_" + time.strftime('%Y-%m-%d',time.localtime()) + ".mp3", 'wb') as f:
            f.write(result)
    if __name__ == '__main__':
        resp=urlopen(url)
        soup=BeautifulSoup(resp,'html.parser')

        text = soup.find_all('ul',class_="list-paddingleft-2")

        i = 1
        for GetText in text:
            print(GetText.get_text())
            OutText = GetText.get_text()
            result  = client.synthesis(str(OutText)+'。', 'zh', 1, {
                'vol': 10,
                'spd': 4,
            })
            # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
            if not isinstance(result, dict):                
                with open('News_'+time.strftime('%Y-%m-%d',time.localtime())+'/News_'+ str(i) +"_" + time.strftime('%Y-%m-%d',time.localtime()) + ".mp3", 'wb') as f:
                    f.write(result)
            i+=1
        
GetArticle()

def GetWeather():
    if __name__ == '__main__':
        resp=urlopen('http://www.weather.com.cn/weather/101260515.shtml')
        soup=BeautifulSoup(resp,'html.parser')
        tagToday=soup.find('p',class_="tem")  #第一个包含class="tem"的p标签即为存放今天天气数据的标签
        try:
            temperatureHigh=tagToday.span.string  #有时候这个最高温度是不显示的，此时利用第二天的最高温度代替。
        except AttributeError as e:
            temperatureHigh=tagToday.find_next('p',class_="tem").span.string  #获取第二天的最高温度代替

        temperatureLow=tagToday.i.string  #获取最低温度
        weather=soup.find('p',class_="wea").string #获取天气
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
        if(os.path.exists('Weathers_'+time.strftime('%Y-%m-%d',time.localtime()))== False):
            os.mkdir('Weathers_'+time.strftime('%Y-%m-%d',time.localtime()))
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('Weathers_'+time.strftime('%Y-%m-%d',time.localtime())+'/weather_'+time.strftime('%Y-%m-%d',time.localtime())+'.mp3', 'wb') as f:
                f.write(result)
GetWeather()