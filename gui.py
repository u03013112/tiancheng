# -*- coding: utf-8 -*- 

import tkinter as tk

from tkinter import ttk


win = tk.Tk()
win['bg']='pink'


barFrame = tk.Frame(win,height=80,width=320,bg='#FFB6CB')
barFrame.pack()

def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)
    tv.heading(col,command=lambda: treeview_sort_column(tv, col, not reverse))

infoFrame = tk.Frame(win,height=960,width=320,bg='#FFB6C1')
infoFrame.pack()
    
columns = [ "Title", "hot", "type"]
tree = ttk.Treeview(infoFrame, columns=columns, show="headings")
for col in columns:
    tree.heading(col,text=col,command=lambda col=col:treeview_sort_column(tree,col,False))             #行标题
    tree.column(col,width=80,anchor='w')   #每一行的宽度,'w'意思为靠右
tree.column("Title", width=100, anchor="center")
tree.column("hot", width=100, anchor="center")
tree.column("type", width=100, anchor="center")
tree.heading("Title", text="Title")
tree.heading("hot", text="hot")
tree.heading("type", text="type")
tree.place(relx=0.004, rely=0.028, relwidth=0.964, relheight=0.95)

ybar=tk.Scrollbar(infoFrame,orient='vertical',command=tree.yview)
ybar.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
tree.configure(yscrollcommand=ybar.set)
# tree.bind()
# for i in range(100):
#     tree.insert("",0,values=[str(i),str(i+10),str(i-10)])
    
win.mainloop()