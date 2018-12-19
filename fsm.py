from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_message
import time
import data
import random
from data import url
chosenMemb = data.membDict['張祐禎']
none_flag = 0
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
    def is_going_to_user(self, event):
        if event.get("message"):
            text = event['message']['text']
            # return text.lower() == 'ha'
            return True
        return False
    def is_going_to_askMemb(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text.find('成員') > -1 or text.find('球員') > -1:
                return True
        return False
    def is_going_to_showMembInfo(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text.lower().find('不用')>-1 or text.lower().find('算了')>-1 or text.lower().find('no')>-1 or text.lower().find('其他問題')>-1 or text.lower().find('沒')>-1:
                sender_id = event['sender']['id']
                responese = send_text_message(sender_id, "好的，有問題可以再問我哦~")
                self.go_back()
                return False
            if data.membDict.get(text)!=None:
                global chosenMemb
                chosenMemb = data.membDict[text]          
                return True
            else:
                global none_flag
                none_flag=1
                return True
            # for i in range(0,len(member)):
                # if text.find(member[i]) > -1:
                #     global chosenMemb
                #     chosenMemb = member[i]

        return False
    # def is_going_to_askMoreMemb(self, event):
    #     if event.get("message"):
    #         text = event['message']['text']
    #         if text.find('成員') > -1:
    #             return True
    #     return False        

    def is_going_to_askRecord(self, event):
        if event.get("message"):     
            text = event['message']['text']
            if text.find('戰績') > -1:
                return True
            # return text.lower() == '我想問系排歷屆戰績'
        return False
    def is_going_to_funPhoto(self, event):
        if event.get("message"):     
            text = event['message']['text']
            if text.find('梗圖') > -1:
                return True
        return False       
    def on_enter_user(self, event):
        print("I'm entering user state")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你好啊!我是系排吉祥物-巨石彥瑋哦！很高興為你服務^^！\n可以詢問我一些關於系排的事情哦，只要是我能回答你的我都很樂意幫忙哦！\n(輸入提示：成員、戰績、系排趣事、梗圖）")
    def on_enter_askMemb(self, event):
        print("I'm entering state1")
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "你想問哪個球員呢？")
    def on_enter_funPhoto(self, event):
        print("I'm entering funPhoto")
        rand = random.randint(0,len(url))
        sender_id = event['sender']['id']
        
        responese = send_text_message(sender_id, "好的 稍等我一下！")  
        responese = send_image_message(sender_id,url[rand])
        self.go_back()

    def on_enter_showMembInfo(self, event):
        print("I'm entering state1")
        sender_id = event['sender']['id']
        global none_flag
        if none_flag!=1:
            responese = send_text_message(sender_id,"球員:"+chosenMemb.name+"\n"+"性別:"+chosenMemb.gender+'\n'+"年級:"+chosenMemb.grade+'\n'+"擅長位置:"+chosenMemb.place+'\n'+"介紹:\n"+chosenMemb.intro)
            responese = send_image_message(sender_id,chosenMemb.url)
        else:
            responese = send_text_message(sender_id,'沒有這位球員哦')
            none_flag = 0
        time.sleep(2)
        responese = send_text_message(sender_id, "還想問哪個球員嗎？")      

        # responese = send_text_message(sender_id, "還有問題想問可以再問我哦！")

    # def on_enter_askMoreMemb(self, event):
    #     sender_id = event['sender']['id']
    #     responese = send_text_message(sender_id, "還想問哪個球員嗎？")      

    def on_enter_askRecord(self, event):
        print("I'm entering state2")
        rec2018 = "2018年 成功盃-冠軍\n2018年 系際盃-八強\n2018年 工院盃-八強\n2018年 大資盃-季軍\n"
        rec2017 = "2017年 聯賽  -八強\n2017年 大資盃-亞軍\n2017年 南資盃-季軍\n2017年 工院盃-冠軍\n2017年 超系盃-季軍\n"
        rec2016 = "2016年 大資盃-季軍\n2016年 工院盃-季軍\n2016年 系際盃-冠軍"
        line = "------------------\n"
        record = rec2018+line+rec2017+line+rec2016
        sender_id = event['sender']['id']
        send_text_message(sender_id, "近年來戰績如下:\n"+record+"\n厲害吧厲害吧><")
        self.go_back()
