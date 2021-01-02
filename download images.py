SMILES_URL='https://skypefan.ru/smajly/'
from bs4 import BeautifulSoup
import requests,os
soup = BeautifulSoup(requests.get(SMILES_URL).text, 'lxml')
res=soup.find_all('img')
imgs=[]
for i in res:
	imgs.append(i['src'])
if not os.path.isdir('images/'):
	os.mkdir('images')
os.chdir('images')
for i in range(len(imgs)):
	try:
		idt=requests.get(imgs[i],stream=True).content
		try:
			file=imgs[i].split('/')[-1]
			if file.find('?')!=-1:
				file=file[:file.find('?')]
			file=str(i+1)+'_'+file
			print(i+1,':',file)
			f=open(file,'wb')
			f.write(idt)
			f.close()
		except IOError:
			pass
	except requests.exceptions.RequestException:
		pass
