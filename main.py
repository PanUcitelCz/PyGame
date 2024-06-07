import pygame

# Je nutné importovat knihovnu pygame
# Na začátku je potřeba pygame nainstalovat pomocí příkazi pip install pygame

# Incializace pygame
pygame.init()


# Vytvoření obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height)) # Nastavíme si velikost herního okna, v závorce je to z důvodu, že se jedná o tak zvaný couples neboli dvojici
pygame.display.set_caption("Naše první hra") # Nastavíme název hry v okně

player = pygame.Rect((300, 250, 50, 50))

# Hlavní herní cyklus
lets_continue = True


    # Vytvoření hodin
clock = pygame.time.Clock()

    # Cyklem while udržujeme hru v běhu, nezapomeňte, že python čte kod ze zhora dolů
while lets_continue:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), player)
    
    key = pygame.key.get_pressed()
    
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    
    
    # Pomocí cyklu for s přomenou event (jako událost) controlujeme veškeré události v event.get(Zde nám knihovna pygame inicializuje veškeré události ve hře)
    for event in pygame.event.get():
        #print(event) # Vypíše mi veškeré eventy při hře do terminálu

        # Pokud se klikne na křížek v okně, zavře se nám hra. Křížek voláme pomocí pygame.QUIT
        if event.type == pygame.QUIT:
            lets_continue = False # Tímto ukončíme cyklus
            
    pygame.display.update()
    
    # Omezení snímkové frekvence na 60 FPS
    clock.tick(60)

# Ukončení pygame
pygame.quit()