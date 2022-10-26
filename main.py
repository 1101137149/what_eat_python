import tkinter as tk #GUI圖型介面工具包 as命名小名可簡化名稱

def createWindow():
    window=tk.Tk() #建立一個視窗實體
    window.title("這是我的第一個視窗") #視窗的title名稱
    btn=tk.Button(window,text="請按我",padx=20,pady=20,font=('arial',16)) #放在window變數裡，按鈕顯示請按我 按鈕內行距長寬20px
    btn.pack(padx=50,pady=30) #視窗大小 寬50 高30
    window.mainloop()


def main():
    createWindow()

if __name__ =="__main__":
    main()