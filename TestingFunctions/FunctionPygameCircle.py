import math
import pygame

from TestingFunctions.FunctionExample import FunctionExample


class FunctionPygameCircle(FunctionExample):
    def __init__(self, data_len, width=500, height=500, dot_size=5):
        self.angle = (2 * math.pi) / (data_len)
        self.width = width
        self.height = height
        self.dot_size = dot_size

    def setup(self):
        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.key.set_repeat(100, 50)
        self.screen.fill([0, 0, 0])

    def run(self, data):
        return pygame.draw.circle(self.screen, [150, 0, 150],
                                  [int(self.width / 2 - math.cos(self.angle * data) * (self.width / 2 - self.dot_size)),
                                   int(self.height / 2 - math.sin(self.angle * data) * (
                                               self.height / 2 - self.dot_size))],
                                  self.dot_size)

    def run_no_return(self, data):
        pygame.draw.circle(self.screen, [150, 0, 150],
                           [int(self.width / 2 - math.cos(self.angle * data) * (self.width / 2 - self.dot_size)),
                            int(self.height / 2 - math.sin(self.angle * data) * (self.height / 2 - self.dot_size))],
                           self.dot_size)

    def reset(self):
        pygame.display.flip()
        self.screen.fill([0, 0, 0])

    def close(self):
        pygame.quit()
