"""
    @Time : 2022/09/04
    @Author : YU.J.P
    @Project : 桌面级时间显示 大气简约美观
    @Declare : CSDN 学习得来 需要安装 pyautogui,pywin32,pillow
    @Version : V 1.3
    Updating :
        2022/09/08 - 选项卡更新 [中文显示/字体显示颜色]
        2022/09/12 - 显示更新 [放大显示，桌面组件模式]
"""


import pyautogui
import datetime
import tkinter as tk


# clock类
class Clock(tk.Tk):
    def __init__(self) -> None:
        """初始化"""
        self.backgroundlabel = None
        self.width = 1080 * 2 // 3
        self.fw, self.fh = pyautogui.size()  # 屏幕大小
        self.height = 73
        self.showSelect = 0  # 全屏显示变量 0:默认,1:半全屏,2:全屏
        super().__init__()
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.transBool = True
        self.backgroundColor = "black"
        self.x, self.y = 0, 0  # 窗口初始位置
        self.clockLen = 26  # 显示字符串长度
        self.window_size = '265x10'
        self.configure(bg=self.backgroundColor)
        self.time_text = "0000-00-00 00:00:00 XXXX"
        self.overrideredirect(1)
        self.font = "Impact"  # 默认字体
        self.fontColor = "pink"  # 字体颜色
        self.fontsize = 30  # 字体大小
        self.attributes("-alpha", 0.37)  # 初始化 半透明

        # 函数
        def addl(event):  # 秒数加 1
            if self.clockLen < 26:
                self.clockLen += 1

        def dell(event):  # 秒数减 1
            if self.clockLen > 19:
                self.clockLen -= 1

        # 默认小屏
        def defaultShow():
            self.showSelect = 0
            self.window_size = "265x10"
            self.width = 1080 * 2 // 3
            self.height = 73
            self.fontsize = 30
            self.clockLen = 26
            self.attributes("-alpha", 0.37)  # 初始化 半透明

        # 半全屏
        def halfFull():
            self.showSelect = 1
            self.window_size = str(self.width) + "x" + str(self.height)
            self.width = 1420
            self.height = 440
            self.fontsize = 110
            self.clockLen = 19
            self.geometry(f"{self.fw}x{self.fh}+0+0")
            self.attributes("-alpha", 0.25)  # 初始化 半透明

        # 全屏
        def activateFull():
            # 0:默认,1:半全屏,2:全屏
            self.showSelect = 2
            self.window_size = str(self.width) + "x" + str(self.height)
            self.width = self.fw
            self.height = self.fh
            self.fontsize = 110
            self.clockLen = 19
            self.geometry(f"{self.fw}x{self.fh}+0+0")
            self.attributes("-alpha", 0.37)  # 初始化 半透明

        # 设置字体
        def setfontmc():
            self.font = "Monotype Corsiva"

        def setfontarial():
            self.font = "Ink Free"

        def setfontdigital():
            self.font = "ds-digital"

        def setfontimpact():
            self.font = "Impact"

        def setfontcomic():
            self.font = "Comic Sans MS"

        def setfontarialn():
            self.font = "Arial"

        def setfonttimes():
            self.font = "Times New Roman"

        # 设置字体颜色
        def setfontCyan():
            self.fontColor = "cyan"

        def setfontPink():
            self.fontColor = "pink"

        def setfontRed():
            self.fontColor = "red"

        def setfontGreen():
            self.fontColor = "green"

        def setfontYellow():
            self.fontColor = "yellow"

        def setfontBlue():
            self.fontColor = "blue"

        def setfontWhite():
            self.fontColor = "white"

        def setfontPurple():
            self.fontColor = "purple"


        # 颜色，本来用lambda实现，但不知道为什么不行
        def colorblack():
            self.backgroundColor = "black"

        def colorgrey():
            self.backgroundColor = "#333333"

        def colorwhite():
            self.backgroundColor = "white"

        def colorblue():
            self.backgroundColor = "blue"

        def colorgreen():
            self.backgroundColor = "green"

        def coloryellow():
            self.backgroundColor = "yellow"

        def colorred():
            self.backgroundColor = "red"

        def colorpurple():
            self.backgroundColor = "purple"

        def quitwin(event):
            self.quit()

        def settrans():  # 半透明
            if self.transBool == False:
                self.attributes("-alpha", 0.37)
            else:
                self.attributes("-alpha", 1)
            self.transBool = not self.transBool

        """主菜单"""
        menubar = tk.Menu(self, activeborderwidth=3)
        xMenu = tk.Menu(menubar, tearoff=False)  # 字体更改菜单
        zMenu = tk.Menu(menubar, tearoff=False)  # 字体颜色更改菜单
        yMenu = tk.Menu(menubar, tearoff=False)  # 背景颜色更改菜单
        oMenu = tk.Menu(menubar, tearoff=False)  # 显示模式更改菜单
        # 字体更改菜单
        xMenu.add_command(label="Ink Free", command=setfontarial)
        xMenu.add_command(label="Monotype Corsiva", command=setfontmc)
        xMenu.add_command(label="Ds-Digital", command=setfontdigital)
        xMenu.add_command(label="Impact", command=setfontimpact)
        xMenu.add_command(label="Comic Sans MS", command=setfontcomic)
        xMenu.add_command(label="Arial", command=setfontarialn)
        xMenu.add_command(label="Times New Roman", command=setfonttimes)
        # 字体颜色更改菜单
        zMenu.add_command(label="cyan", command=setfontCyan)
        zMenu.add_command(label="pink", command=setfontPink)
        zMenu.add_command(label="red", command=setfontRed)
        zMenu.add_command(label="green", command=setfontGreen)
        zMenu.add_command(label="yellow", command=setfontYellow)
        zMenu.add_command(label="blue", command=setfontBlue)
        zMenu.add_command(label="white", command=setfontWhite)
        zMenu.add_command(label="purple", command=setfontPurple)
        # 背景颜色更改菜单
        yMenu.add_command(label="Red", command=colorred)
        yMenu.add_command(label="Blue", command=colorblue)
        yMenu.add_command(label="Green", command=colorgreen)
        yMenu.add_command(label="Yellow", command=coloryellow)
        yMenu.add_command(label="Black", command=colorblack)
        yMenu.add_command(label="Grey", command=colorgrey)
        yMenu.add_command(label="Purple", command=colorpurple)
        yMenu.add_command(label="White", command=colorwhite)
        # 显示模式更改菜单
        oMenu.add_command(label="小屏显示", command=defaultShow)
        oMenu.add_command(label="放大显示", command=halfFull)
        oMenu.add_command(label="全屏显示", command=activateFull)

        # 显示字体选项
        menubar.add_cascade(label="字体", menu=xMenu, font=("FangSong", 10))
        # 显示字体颜色选项
        menubar.add_cascade(label="字体色", menu=zMenu, font=("FangSong", 10))
        # 显示背景颜色选型
        menubar.add_cascade(label="背景色", menu=yMenu, font=("FangSong", 10))
        # 显示屏幕模式选型
        menubar.add_cascade(label="显示模式", menu=oMenu, font=("FangSong", 10))
        # 显示透明选项
        menubar.add_checkbutton(label="非透明显示", command=settrans, font=("FangSong", 10))
        # 退出程序 快捷键 ctrl + Q
        menubar.add_command(label="退出程序", command=self.quit, font=("FangSong", 10), accelerator="Ctrl+Q")

        def xShowMenu(event):
            menubar.post(event.x_root, event.y_root)

        self.bind("<Button-3>", xShowMenu)
        self.bind("<B1-Motion>", self.move)
        self.bind("<Right>", addl)
        self.bind("<Left>", dell)
        self.bind("<Control-Q>", quitwin)
        self.bind("<Control-q>", quitwin)

        # 显示标签
        self.lbl = tk.Label(self,
            text=self.time_text,
            font=(self.font, self.fontsize),
            anchor="sw",
            background="#333333",
            foreground="pink")
        self.lbl.pack()
        self.update_time()  # 更新。。。

    # 鼠标拖动移动
    def move(self, event):
        if self.showSelect == 0 or self.showSelect == 1:
            self.geometry(
                f"{self.width}x{self.height}+{(event.x - self.x) + self.winfo_x()}+{(event.y - self.y) + self.winfo_y()}")
        pass

    # 更新时间操作
    def update_time(self):

        # 年 月 日
        self.geometry(f"{self.width}x{self.height}")
        yy = int(str(datetime.datetime.now())[:4])
        mm = int(str(datetime.datetime.now())[5:7])
        dd = int(str(datetime.datetime.now())[8:10])
        k = datetime.date(yy, mm, dd).weekday()
        self.lbl.focus_set()

        if self.showSelect == 1 or self.showSelect == 2:  # 全屏
            self.lbl.config(
                anchor="sw",
                text=("\n" + str(datetime.datetime.now())[:10] +
                "\n" + " " + self.days[k] + str(datetime.datetime.now())[10:self.clockLen]),
                font=(self.font, self.fontsize),
                foreground=self.fontColor,
                background=self.backgroundColor
            )
        elif self.showSelect == 0:
            # 未显示秒数后的小数[:self.clockLen - 7]
            self.lbl.config(
                anchor="sw",
                text=(str(datetime.datetime.now())[:self.clockLen - 7] + " " + self.days[k]),
                font=(self.font, self.fontsize),
                foreground=self.fontColor,
                background=self.backgroundColor
            )

        self.after(100, self.update_time)  # 0.1s 更新操作
        self.configure(bg=self.backgroundColor)


# 运行
if __name__ == "__main__":
    Clock().mainloop()
