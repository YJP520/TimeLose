"""
    Time : 2022/09/04
    Author : YU.J.P
    Project : 桌面级时间显示 大气简约美观
"""

import time  # 获取时间
import tkinter # 窗口视窗
from tkinter import messagebox  # 消息窗口
from tkinter import ttk  # 下拉选择框

# 全局变量
VERSION = 'Time V1.0'  # 版本信息


class myTime:
    def __init__(self):
        self.nowYear = None  # 年
        self.nowMonth = None  # 月
        self.nowDay = None  # 日
        self.nowHour = None  # 时
        self.nowMinute = None  # 分
        self.nowSecond = None  # 秒
        self.setTime()

    # 时间更新
    def setTime(self):
        nowTime = time.gmtime()  # 世界统一时间
        self.nowYear = nowTime[0]  # 年
        self.nowMonth = nowTime[1]  # 月
        self.nowDay = nowTime[2]  # 日
        self.nowHour = nowTime[3] + 8  # 时
        self.nowMinute = nowTime[4]  # 分
        self.nowSecond = nowTime[5]  # 秒

    # 循环运行
    def start(self):
        nowTime = myTime()
        while True:
            print('{0}/{1}/{2}'.format(nowTime.nowYear, nowTime.nowMonth, nowTime.nowDay))
            print('{0}:{1}:{2}'.format(nowTime.nowHour, nowTime.nowMinute, nowTime.nowSecond))
            time.sleep(1)  # 延迟 1s
            self.setTime()  # 更新时间


# 主要逻辑运行
class MainGUI:
    # 固定变量
    window_0 = None  # 窗口 编号:0
    window_0_width = 500  # 窗口宽度
    window_0_height = 300  # 窗口宽度
    label_0 = None  # 标签 编号:0 文本显示

    def __init__(self):
        # 窗口初始化
        self.initALLWindow()
        # 标签初始化
        self.initAllLable()


    # 窗口初始化
    def initALLWindow(self):
        # 窗口 编号:0 初始化
        MainGUI.window_0 = tkinter.Tk()  # 创建窗口
        MainGUI.window_0.title(VERSION)  # 窗口命名
        MainGUI.window_0.geometry(str(MainGUI.window_0_width) + 'x' +
            str(MainGUI.window_0_height) + '+500+200')  # 设置窗口大小 -- 格式 : '长x宽+x+y'


    # 文本显示
    def initAllLable(self):
        # 标签 编号:0 初始化
        MainGUI.label_0 = tkinter.Label(self.window_0, text='封茗囧菌( • ̀ω•́ )✧', font=('dengxian', 16), background='pink')
        MainGUI.label_0.place(x=100, y=50, width=300, height=50)

    # 主程序入口
    def Start(self):
        # 循环显示窗口
        MainGUI.window_0.mainloop()

# 运行
if __name__ == '__main__':
    myTime().start()
