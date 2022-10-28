import tkinter as tk #視窗
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter.font as tkFont
import requests 
import json


#標籤
class TKLable(tk.Label):
    def __init__(self,parents,**kwargs):
        super().__init__(parents,**kwargs)
        helv26=tkFont.Font(family='微軟正黑體',size=18,weight='bold') #先設定字體格式
        self.config(font=helv26,bg= '#345678',foreground="#FFFFFF")

#圖片按鈕
class ImageButton(tk.Button):
    def __init__(self,imgUrl,parents,**kwargs): #**kwargs 打包
        super().__init__(imgUrl,parents,**kwargs) #**kwargs 打開
        btnimage1=Image.open(imgUrl)
        self.tkbtnImage1=ImageTk.PhotoImage(btnimage1)
        self.config(image=self.tkbtnImage1,borderwidth=0)


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        mainFrame = tk.Frame(self,bg='#345678',width=800,height=500)
        mainFrame.pack()


def main():
    window=Window()
    window.title("今天吃什麼?")
    window.resizable(0,0) #禁止拖拉視窗調整視窗大小
    window.geometry("800x500")


   # label text for title
    TKLable(window, text = "??今天吃什麼??").place(x=300,y=0)

# label
    TKLable(window, text = "請選擇地區:").place(x=200,y=200)


# Combobox creation
    n = tk.StringVar()
    monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)

# Adding combobox drop down list
    monthchoosen['values'] = (' January',
						' February',
						' March',
						' April',
						' May',
						' June',
						' July',
						' August',
						' September',
						' October',
						' November',
						' December')

    monthchoosen.place(x=400,y=200)
    monthchoosen.current()
    window.mainloop()



if __name__ =="__main__":
    main()

