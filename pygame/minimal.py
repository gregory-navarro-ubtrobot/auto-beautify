import pygame
def main():
    pygame.init()
    map = pygame.image.load("/home/administrator/Documents/research/Auto-Beautify/simple-webpage/assets/map.png")
    pygame.display.set_icon(map)
    pygame.display.set_caption("minimal program")

    screen = pygame.display.set_mode((240, 180))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
