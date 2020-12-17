import tkinter as tk
import random, time
root=tk.Tk()
root.title('Игра в числа')
class Val:
	def __init__(self,val=None):
		self.value=val
v=Val(random.randint(1,100))
rs=Val(0)
def chck():
	vld=1
	try:
		int(ua.get())
	except:
		vld=0
	if rs.value:
		beg.value=time.time()
		ua.config(state='normal')
		ua.delete(0,'end')
		b.config(text='ОК')
		lbl.config(text='')
		title.config(text='Я загадал(а) число от 1 до 100 включительно. Угадаете его?')
		rs.value=0
	elif not vld:
		lbl.config(text='Не число. Попытка не считается.')
		ua.delete(0,'end')
	elif int(ua.get())<v.value:
		lbl.config(text='Моё число больше, чем %s.'%ua.get())
		ua.delete(0,'end')
		mod.value+=1
	elif int(ua.get())>v.value:
		lbl.config(text='Моё число меньше, чем %s.'%ua.get())
		ua.delete(0,'end')
		mod.value+=1
	else:
		lbl.config(text='Вы угадали число %s! Затрачено %s попыток и %s секунд.'%(ua.get(),mod.value+1,round(time.time()-beg.value)))
		title.config(text='Вы угадали число от 1 до 100 включительно!')
		b.config(text='Новая игра')
		ua.config(state='disabled')
		v.value=random.randint(1,100)
		mod.value=0
		rs.value=1
mod=Val(0)
game=tk.Frame(root)
title=tk.Label(root,text='Я загадал(а) число от 1 до 100 включительно. Угадаете его?')
title.pack()
ua=tk.Entry(game)
ua.grid(row=1,column=1)
b=tk.Button(game,text='OK',command=chck)
b.grid(row=1,column=2)
b.config(text='Новая игра')
ua.config(state='disabled')
rs.value=1
lbl=tk.Label(game)
lbl.grid(row=2,column=1)
game.pack()
beg=Val(0)
root.mainloop()