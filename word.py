import requests
from tkinter import Tk,Label,Button,Entry,Frame
from random import choice
class Val:
	def __init__(self,value=None):
		self.val=value
def check(word):
	if word.strip()=='':
		return False,'ты пропустил(а) слово'
	params = {'text':word, 'lang':'ru'}
	r = requests.get('http://speller.yandex.net/services/spellservice.json/checkText', params=params)
	if len(r.json())>0:
		return False,'«'+[v for v in r.json()[0]['s']][0]+'»'
	else:
		return True,''
root=Tk()
root.title('Составь из слова')
score=Val(0)
full=Val(choice(['теплостанция','смекалка','редактирование','подготовка','переадресация','закодирование','безупречность','покупатель','мюнгхаузен','стоматология','информация','учительница','астронавт']))
lfl=Label(root,text='Из «'+full.val+'»')
lfl.pack()
lst=[full.val]
sc=Label(root,fg='#ff0000')
sc.pack()
frm=Frame(root)
frm.pack()
wrd=Entry(frm)
wrd.grid(row=1,column=1)
out=Label(root)
out.pack()
def nxt():
	val=wrd.get()
	wrd.delete(0,'end')
	wrd.insert('end',val.lower())
	res=check(wrd.get())
	if res[0]:
		fv=full.val
		for i in wrd.get():
			if not i in fv:
				out.config(text=f'Нет. Нельзя «{i}»')
				break
			fv=list(fv)
			fv.remove(i)
			fv=''.join(fv)
		else:
			if not wrd.get() in lst:
				lst.append(wrd.get())
				score.val+=1
				sc.config(text=score.val*'★')
				out.config(text='Да!!!')
			else:
				out.config(text='Уже было.')
	else:
		if res[1].lower()==wrd.get():
			out.config(text='Имена собственные запрещены!')
		else:
			out.config(text='Нет такого слова. Наверное, '+res[1])
ok=Button(frm,text='OK',command=nxt)
ok.grid(row=1,column=2)
root.mainloop()