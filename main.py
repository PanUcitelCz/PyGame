import pygame

# Je nutné importovat knihovnu pygame
# Na začátku je potřeba pygame nainstalovat pomocí příkazi pip install pygame

# Incializace pygame
pygame.init()


# Vytvoření obrazovky
width = 600
height = 300
screen = pygame.display.set_mode((width, height)) # Nastavíme si velikost herního okna, v závorce je to z důvodu, že se jedná o tak zvaný cuple neboli dvojici
pygame.display.set_caption("Naše první hra") # Nastavíme název hry v okně

# Hlavní herní cyklus
lets_continue = True

    # Cyklem while udržujeme hru v běhu, nezapomeňte, že python čte kod ze zhora dolů
while lets_continue:
    # Pomocí cyklu for s přomenou event (jako událost) controlujeme veškeré události v event.get(Zde nám knihovna pygame inicializuje veškeré události ve hře)
    for event in pygame.event.get():
        print(event) # Vypíše mi veškeré eventy při hře do terminálu

        # Pokud se klikne na křížek v okně, zavře se nám hra. Křížek voláme pomocí pygame.QUIT
        if event.type == pygame.QUIT:
            lets_continue = False # Tímto ukončíme cyklus

# Ukončení pygame
pygame.quit()