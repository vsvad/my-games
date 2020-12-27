SMILES_URL='https://skypefan.ru/smajly/'
from bs4 import BeautifulSoup
import requests,os
from PIL import Image
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
		idt=requests.get(imgs[i],stream=True).raw
		try:
			img=Image.open(idt)
			img.save(str(i+1)+'.png')
			print(i+1)
		except IOError:
			pass
	except requests.exceptions.RequestException:
		pass
