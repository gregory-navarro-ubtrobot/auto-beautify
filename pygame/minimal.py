import pygame
def main():
    pygame.init()
    map = pygame.image.load("map.png")
    print(map)
    pygame.display.set_icon(map)
    pygame.display.set_caption("minimal program")
    size = (832, 768)
    screen = pygame.display.set_mode(size)
    screen.blit(map, (0, 0))
    pygame.display.update()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()

