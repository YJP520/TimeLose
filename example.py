#
# 需要安装 pyautogui,pywin32,pillow
#
# CSDN 学习得来
#

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
        self.fontsize = 20  # 字体大小
        self.fullbool = True
        super().__init__()
        self.days = ["Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.transbool = True
        self.backgroundcolor = "black"
        self.x, self.y = 0, 0
        self.clocklen = 26
        self.window_size = '265x10'
        self.attributes("-topmost", 1)
        self.configure(bg=self.backgroundcolor)
        self.time_text = ""
        self.overrideredirect(1)
        self.font = "Impact"  # 默认字体
        self.attributes("-alpha", 1)

        # 函数
        def addl(event):  # 秒数加1
            if self.clocklen < 26:
                self.clocklen += 1

        def dell(event):  # 秒数减1
            if self.clocklen > 19:
                self.clocklen -= 1

        # 全屏
        def activatefull():
            if self.fullbool == True:
                self.window_size = str(self.width) + "x" + str(self.height)
                self.width = self.fw
                self.height = self.fh
                self.fontsize = 110
                self.clocklen = 19
                self.geometry(f"{self.fw}x{self.fh}+0+0")
            else:
                self.window_size = "265x10"
                self.width = 1040
                self.height = 73
                self.fontsize = 20
                self.clocklen = 26
            self.fullbool = not self.fullbool

        # 设置字体
        def setfontmc():
            self.font = "Monotype Corsiva"

        def setfontarial():
            self.font = "Ink Free"

        def setfontdigital():
            self.font = "ds-digital"

        def setfontimpact():
            self.font = "Impact"

        def setfontsegoe():
            self.font = "Impact"

        def setfontcomic():
            self.font = "Comic Sans MS"

        def setfontarialn():
            self.font = "Arial"

        def setfonttimes():
            self.font = "Times New Roman"

        # 颜色，本来用lambda实现，但不知道为什么不行
        def colorblack():
            self.backgroundcolor = "black"

        def colorgrey():
            self.backgroundcolor = "#333333"

        def colorwhite():
            self.backgroundcolor = "white"

        def colorblue():
            self.backgroundcolor = "blue"

        def colorgreen():
            self.backgroundcolor = "green"

        def coloryellow():
            self.backgroundcolor = "yellow"

        def colorred():
            self.backgroundcolor = "red"

        def colorpurple():
            self.backgroundcolor = "purple"

        def quitwin(event):
            self.quit()

        def settrans():  # 半透明
            if self.transbool == True:
                self.attributes("-alpha", 0.37)
                self.attributes("-alpha", 0.37)
            else:
                self.attributes("-alpha", 1)
                self.attributes("-alpha", 1)
            self.transbool = not self.transbool

        """主菜单"""
        menubar = tk.Menu(self, activeborderwidth=3)
        xMenu = tk.Menu(menubar, tearoff=False)
        yMenu = tk.Menu(menubar, tearoff=False)
        xMenu.add_command(label="Ink Free", command=setfontarial)
        xMenu.add_command(label="Monotype Corsiva", command=setfontmc)
        xMenu.add_command(label="Ds-Digital", command=setfontdigital)
        xMenu.add_command(label="Impact", command=setfontimpact)
        xMenu.add_command(label="Segoe UI Black", command=setfontsegoe)
        xMenu.add_command(label="Comic Sans MS", command=setfontcomic)
        xMenu.add_command(label="Arial", command=setfontarialn)
        xMenu.add_command(label="Times New Roman", command=setfonttimes)

        yMenu.add_command(label="Red", command=colorred)
        yMenu.add_command(label="Blue", command=colorblue)
        yMenu.add_command(label="Green", command=colorgreen)
        yMenu.add_command(label="Yellow", command=coloryellow)
        yMenu.add_command(label="Black", command=colorblack)
        yMenu.add_command(label="Grey", command=colorgrey)
        yMenu.add_command(label="Purple", command=colorpurple)
        yMenu.add_command(label="White", command=colorwhite)

        menubar.add_cascade(label="Change Font", menu=xMenu, font=("ds-digital", 10))
        menubar.add_cascade(label="Change Background Color", menu=yMenu, font=("ds-digital", 10))
        menubar.add_checkbutton(label="Translucent", command=settrans, font=("ds-digital", 10))
        menubar.add_command(label="Quit Clock", command=self.quit, font=("ds-digital", 10), accelerator="Ctrl+Q")
        menubar.add_checkbutton(label="Full Screen", command=activatefull, font=("ds-digital", 10))

        def xShowMenu(event):
            menubar.post(event.x_root, event.y_root)

        self.bind("<Button-3>", xShowMenu)
        self.bind("<B1-Motion>", self.move)
        self.bind("<Right>", addl)
        self.bind("<Left>", dell)
        self.bind("<Control-Q>", quitwin)
        self.bind("<Control-q>", quitwin)

        self.lbl = tk.Label(self,
            text=self.time_text + "sadsadsadsadsa",
            font=(self.font, 20),
            anchor="sw",
            background="#333333",
            foreground="cyan")
        self.lbl.pack()
        self.update_time()

    def move(self, event):
        if self.fullbool:
            self.geometry(
                f"{self.width}x{self.height}+{(event.x + 7 - self.x) + self.winfo_x()}+{(event.y - self.y) + self.winfo_y()}")
        pass

    def update_time(self):
        # a=self.lbl.winfo_reqheight()
        # b=self.lbl.winfo_reqwidth()

        # 年 月 日
        self.geometry(f"{self.width}x{self.height}")
        yy = int(str(datetime.datetime.now())[:4])
        mm = int(str(datetime.datetime.now())[5:7])
        dd = int(str(datetime.datetime.now())[8:10])
        k = datetime.date(yy, mm, dd).weekday()
        self.lbl.focus_set()

        if self.fullbool == False:
            self.lbl.config(anchor="sw", text=("\n" + str(datetime.datetime.now())[:10] +
                "\n" + str(datetime.datetime.now())[10:self.clocklen] + " " + self.days[k]),
                    font=(self.font, self.fontsize), background=self.backgroundcolor)
        else:
            # 未显示秒数后的小数[:self.clocklen - 7]
            self.lbl.config(anchor="sw", text=(str(datetime.datetime.now())[:self.clocklen - 7] + " " + self.days[k]),
                font=(self.font, self.fontsize), background=self.backgroundcolor)

        self.after(1, self.update_time)
        self.configure(bg=self.backgroundcolor)


if __name__ == "__main__":
    Clock().mainloop()
