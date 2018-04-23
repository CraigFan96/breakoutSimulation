import pygame

pygame.init()

display_width = 800
displaya_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

itemImg = pygame.image.load('item.png')

def item(x, y):
	gameDisplay.blit(itemImg, (x, y))

x = (display_width * 0.45)
y = (display_height * 0.8)

crashed = False

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

	gameDisplay.fill(black)
	item(x, y)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()