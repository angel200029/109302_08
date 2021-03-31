from django.conf import settings
from linebot import LineBotApi
from linebot.models import TextSendMessage
import requests
import twder  #匯率套件

line_bot_api = LineBotApi (settings.LINE_CHANNEL_ACCESS_TOKEN)

currencies = {'美金':'USD','美元':'USD','港幣':'HKD','英鎊':'GBP','GBP':'GBP','澳幣':'AUD','加拿大幣':'CAD',\
              '加幣':'CAD','新加坡幣':'SGD','新幣':'SGD','瑞士法郎':'CHF','瑞郎':'CHF','日圓':'JPY',\
              '日幣':'JPY','南非幣':'ZAR','瑞典幣':'SEK','紐元':'NZD','紐幣':'NZD','泰幣':'THB',\
              '泰銖':'THB','菲國比索':'PHP','菲律賓幣':'PHP','印尼幣':'IDR','歐元':'EUR','韓元':'KRW',\
              '韓幣':'KRW','越南盾':'VND','越南幣':'VND','馬來幣':'MYR','人民幣':'CNY'}  #幣別字典
keys = currencies.keys()

def sendUse(event):  #使用說明
    try:
        text1 ='''查詢匯率：輸入外幣名稱「XXXX」，例如「美金」,「美元」,「港幣」,「英鎊」,「GBP」\
「澳幣」,「加拿大幣」,「加幣」,「新加坡幣」,「新幣」,「瑞士法郎」,「瑞郎」,\
「日圓」,「日幣」,「南非幣」,「瑞典幣」,「紐元」,「紐幣」,「泰幣」,「泰銖」,\
「菲國比索」,「菲律賓幣」,「印尼幣」,「歐元」,「韓元」,「韓幣」,「韓元」,\
「越南盾」,「越南幣」,「馬來幣」,「人民幣」'''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendTWder(event,mtext):
    try:
        #money = '美元'
        money = mtext
        if not money == '': #匯率類幣別存在
            if money in keys:
                rate1 = float(twder.now(currencies[money])[1]) #由匯率套件取得匯率
                rate2 = float(twder.now(currencies[money])[2])
                rate3 = float(twder.now(currencies[money])[3])
                rate4 = float(twder.now(currencies[money])[4])
                message = money + '_現金買入匯率: ' + str(rate1) + '_(台灣銀行端) \n'+money + '_現金賣出匯率: ' + str(rate2) + '_(台灣銀行端) \n'+money + '_即期買入匯率: ' + str(rate3) + '_(台灣銀行端) \n'+money + '_即期賣出匯率: ' + str(rate4) + '_(台灣銀行端) \n'
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='無此幣別匯率資料!'))
        else: #其他未知輸入
            text = '無法了解你的意思，請重新輸入！'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='執行時產生錯誤!'))


      

def neuWeb(event):  #網頁連結
    try:
        text1 ='''
Demo外匯中心網頁:http://fintech.mcu.edu.tw/mcu/?act=shopping&cmd=pavilion&pg_id=2020040200011
                '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

