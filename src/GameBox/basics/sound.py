import pygame

class Sound:
    def __init__(self, path: str, volume: float = 1.0):
        self.sound = pygame.mixer.Sound(path)
        self.volume = volume

    def play(self, loops: int = 0, maxtime: int = 0, fade_ms: int = 0):
        self.sound.play(loops, maxtime, fade_ms)

    def stop(self):
        self.sound.stop()

    def set_volume(self, volume: float):
        self.volume = volume
        self.sound.set_volume(volume)
