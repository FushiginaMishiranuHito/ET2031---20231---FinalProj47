a = int( 10*2/3)
print(a)
import pygame
import pygame as py 
  
# Initiate pygame and the modules that comes with pygame 
py.init() 
  
# setting frame/window/surface with some dimensions 
window = py.display.set_mode((422, 600)) 
  
# to set title of pygame window 
py.display.set_caption("GFG") 
image = pygame.image.load('assets/Starting Tiles.png')

y_image = int(image.get_height()*2/3)
x_image=  int(image.get_width()*2/3)
#x, y = int(image.get_size()*2/3)
image = pygame.transform.scale(image,(x_image, y_image))
while True: 
    window.blit(image, (0, 0)) 
  
    # loop through the list of Event 
    for event in py.event.get(): 
        # to end the event/loop 
        if event.type == py.QUIT: 
  
            # it will deactivate the pygame library 
            py.quit() 
            quit() 
  
        # to display when screen update 
        py.display.flip() 

