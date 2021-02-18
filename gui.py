import tkinter as tk
from tkinter import ttk
from spider import Spider
from show import Show
import time

win = tk.Tk()
win.title('感谢甜橙')
win['bg']='pink'


barFrame = tk.Frame(win,height=30,width=320,bg='#FFB6CB')
barFrame.pack()

def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)
    tv.heading(col,command=lambda: treeview_sort_column(tv, col, not reverse))

infoFrame = tk.Frame(win,height=960,width=320,bg='#FFB6C1')
infoFrame.pack()
    
columns = [ "title", "st", "type","url"]
tree = ttk.Treeview(infoFrame, columns=columns, show="headings")
for col in columns:
    tree.heading(col,text=col,command=lambda col=col:treeview_sort_column(tree,col,False))             #行标题
    tree.column(col,width=80,anchor='w')   #每一行的宽度,'w'意思为靠右
tree.column("title", width=100, anchor="center")
tree.column("st", width=160, anchor="w")
tree.column("type", width=40, anchor="center")
tree.column("url",width=1000, anchor="center")
tree.heading("title", text="标题")
tree.heading("st", text="开播时间")
tree.heading("type", text="类型")
tree.heading("url", text="连接")
tree.place(relx=0.004, rely=0.008, relwidth=0.964, relheight=0.98)

ybar=tk.Scrollbar(infoFrame,orient='vertical',command=tree.yview)
ybar.place(relx=0.971, rely=0.008, relwidth=0.024, relheight=0.958)
tree.configure(yscrollcommand=ybar.set)
def onSelect(event):
    sels= event.widget.selection()#event.widget获取Treeview对象，调用selection获取选择对象名称
    for idx in sels:
        values = tree.item(idx)['values']
        url = values[3]
        show = Show(win,values[0],values[3])
        show.show()
        
tree.bind("<<TreeviewSelect>>", onSelect)
sp = Spider()

def strFilter(string):
    ret=''
    for j in range(len(string)):
        if ord(string[j]) in range(65536): 
            ret=ret+string[j]
        else :
            ret = ret + 'x'
    return ret 

def didReflushBtnClicked():  
    sp.sp()
    x=tree.get_children()
    for item in x:
        tree.delete(item)
    for d in sp.data:
        st = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(d['starttime'])))
        title = strFilter(d['title'])
        if len(title) == 0:
            # title = '无名'
            title = strFilter(d['user_nicename'])
        t='免费'
        if d['type'] != '0':
            t='收费'
        tree.insert("",'end',values=[title,st,t,d['pull']],tags = (t,))
    tree.tag_configure('免费', background='white')
    tree.tag_configure('收费', background='pink')
    countLabel.configure(text='共计：'+str(len(sp.data))+"个可观看直播")
    treeview_sort_column(tree,'st',True)
reflushBtn = tk.Button(barFrame,text='刷新',command=didReflushBtnClicked)
reflushBtn.place(x=5,y=2,width=100, height=26)

countLabel = tk.Label(barFrame,text='<-请点击刷新')
countLabel.place(x=110,y=5)

didReflushBtnClicked()
win.mainloop()