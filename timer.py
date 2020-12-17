import pygame,sys
inv='Start'
play=False
def bcl(cp,rct):
	if cp[0] in range(rct[0],rct[0]+rct[2]+1):
		if cp[1] in range(rct[1],rct[1]+rct[3]+1):
			return True
	return False
c=0.0
pygame.init()
d=pygame.display.set_mode((800,800))
txt=pygame.font.Font(None,100)
while True:
	d.fill((255,255,255))
	tob=txt.render(str(c),0,(0,0,0))
	d.blit(tob,(0,0))
	pygame.draw.rect(d, (255, 0,0), (0, 100, 250, 75))
	tob2=txt.render('Restart',0,(255,255,255))
	d.blit(tob2,(0,100))
	pygame.draw.rect(d, (255, 0,0), (260, 100, 160, 75))
	tob3=txt.render(inv,0,(255,255,255))
	d.blit(tob3,(260,100))
	pygame.display.update()
	if play:
		pygame.time.delay(100)
		c+=0.1
		c=round(c,1)
		c=float(c)
	events=[e.type for e in pygame.event.get()]
	if pygame.QUIT in events:
		pygame.quit()
		sys.exit(0)
	if pygame.MOUSEBUTTONUP in events:
		cl=pygame.mouse.get_pos()
		if bcl(cl,(0,100,250,75)):
			c=0.0
		elif bcl(cl,(260,100,250,75)):
			play=not play
			if play:
				inv='Stop'
			else:
				inv='Start'