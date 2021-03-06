import pygame, sys, time
 
class Game:
    def __init__(self):
        
        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((480,800))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()
 
    def run(self):
        last_time = time.time()
        while True:
            
            # delta time
            dt = time.time() - last_time
            last_time = time.time()
 
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # game logic
            
            pygame.display.update()
            self.clock.tick(120)
 
if __name__ == '__main__':
    game = Game()
    game.run()