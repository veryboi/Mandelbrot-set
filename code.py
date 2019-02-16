


import pygame
import colorsys
clock = pygame.time.Clock()
done = False
MAX_ITER = 80

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n
def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
WIDTH = 600
HEIGHT = 400
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

coordinates = (-0.7463, 0.1102)
while not done:
    RE_START = (RE_START - coordinates[0]) * 0.9 + coordinates[0]
    RE_END = (RE_END - coordinates[0]) * 0.9 + coordinates[0]
    IM_START = (IM_START - coordinates[1]) * 0.9 + coordinates[1]
    IM_END = (IM_END - coordinates[1]) * 0.9 + coordinates[1]


    palette = []
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number

            c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            m = mandelbrot(c)

            hue = m / MAX_ITER
            saturation = 1
            value = 1 if m < MAX_ITER else 0
            #print((hue, saturation, value))
            screen.set_at((x, y), hsv2rgb(hue, saturation, value))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    print("done")
    pygame.display.flip()
    clock.tick(60)
