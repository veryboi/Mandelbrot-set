

from pygame.locals import *
flags = HWSURFACE|DOUBLEBUF|HWACCEL
import pygame
import colorsys
import timeit
from math import log, log2
import math
from decimal import *
getcontext().prec = 1000
clock = pygame.time.Clock()
done = False
MAX_ITER = 80
gradientC = [
(66,30,15),
(25,7,26),
(9,1,47),
(4,4,73),
(0,7,100),
(12,44,138),
(24,82,177),
(57,125,209),
(134,181,229),
(211,236,248),
(241,233,191),
(248,201,95),
(255,170,0),
(204,128,0),
(153,87,0),
(106,52,3)
]

def gradient(degree):
    mi,ma = math.floor(degree*16), math.ceil(degree*16)
    if ma == 16:
        ma = 15
    if mi == 16:
        mi = 15
    miS, maS = gradientC[mi], gradientC[ma]
    percentage = degree*16-mi
    return (miS[0]*percentage+maS[0]*(1-percentage), miS[1]*percentage+maS[1]*(1-percentage), miS[2]*percentage+maS[2]*(1-percentage))
def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1

    if n == MAX_ITER:
        return MAX_ITER

    return n + 1 - log(log2(abs(z)))
WIDTH = 600
HEIGHT = 400
#You can adjust this, just keep the aspect ratio.
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT),flags)
screen.set_alpha(None)



coordinates = (-0.207107867093967732893764544285894983866865721506089742782655437797926445872029873945686503449818426679850 , 1.12275706363259748461604158116265882079904682664638092967742378016679413783606239593843344659123247751651)
#some coordinate I found on the internet. You can put in whatever coordinate you want.

# Plot window
RE_START = coordinates[0]-1.5
RE_END = coordinates[0]+1.5
IM_START = coordinates[1]-1
IM_END = coordinates[1]+1

prev = timeit.default_timer()
multiplier= 0.7
#This dictates how much zoom it does per frame. keep in mind this is logarithmic.
while not done:
    RE_START = (RE_START - coordinates[0]) * multiplier + coordinates[0]
    RE_END = (RE_END - coordinates[0]) * multiplier + coordinates[0]
    IM_START = (IM_START - coordinates[1]) * multiplier + coordinates[1]
    IM_END = (IM_END - coordinates[1]) * multiplier + coordinates[1]


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
            screen.set_at((x, y), gradient(hue))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    print('Time: ',timeit.default_timer() - prev)
    prev = timeit.default_timer()
    pygame.display.flip()
    clock.tick(60)
