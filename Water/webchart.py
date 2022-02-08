import win32gui
import win32con
import win32clipboard as w
from win32gui import *
import os

main = "D:\\sql\\b.exe"
import time
while True:
    titles = set()
    def foo(hwnd, Nouse):
        titles.add(GetWindowText(hwnd))
    EnumWindows(foo, 0)
    if "听风换号树" in titles:#听风换号树  北京-天雨
        w.OpenClipboard()  # 打开剪贴板
        w.EmptyClipboard()  # 清空剪贴板内容。可以忽略这步操作，但是最好加上清除粘贴板这一步
        w.SetClipboardData(win32con.CF_UNICODETEXT, "1122")  # 以Unicode文本形式放入剪切板


        w.CloseClipboard()
        hld = win32gui.FindWindow("ChatWnd", "听风换号树")
        # hld = win32gui.FindWindow("TXGuiFoundation", "北京-天雨") #TXGuiFoundation
        r_v = os.system(main)
        win32gui.SendMessage(hld, 770, 0, 0)

        # msg = "11122"
        # time.sleep(2)
        # w.OpenClipboard()
        # w.EmptyClipboard()
        # w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
        # print('11')
        # win32gui.SendMessage(hld,win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

        # x = random.randrange(1900)
        # y = random.randrange(1200)
        # try:
        # 	win32gui.SetWindowPos(hld, win32con.HWND_TOPMOST, x, y, 400,400, win32con.SWP_SHOWWINDOW)
        # except:
        # 	continue
