#Literally 40x laggier, but allows for way more zoom. requires mpmath module

from pygame.locals import *
flags = HWSURFACE|DOUBLEBUF|HWACCEL
import pygame
import timeit
from math import log, log2
import math
from mpmath import mp, mpf, mpc


mp.dps = 100
size = 0.5
WIDTH = int(600*size)
HEIGHT = int(400*size)
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
coordinates = (mpf(-1.740062382579339905220844167065825638296641720436171866879862418461182919644153056054840718339483225743450008259172138785492983677893366503417299549623738838303346465461290768441055486136870719850559269507357211790243666940134793753068611574745943820712885258222629105433648695946003865), mpf(0.0281753397792110489924115211443195096875390767429906085704013095958801743240920186385400814658560553615695084486774077000669037710191665338060418999324320867147028768983704831316527873719459264592084600433150333362859318102017032958074799966721030307082150171994798478089798638258639934))
#some coordinate I found on the internet. You can put in whatever coordinate you want.

# Plot window
RE_START = coordinates[0]-1.5
RE_END = coordinates[0]+1.5
IM_START = coordinates[1]-1
IM_END = coordinates[1]+1

prev = timeit.default_timer()
multiplier= 0.01
#This dictates how much zoom it does per frame. keep in mind this is logarithmic.

def gradient(degree):
    mi,ma = math.floor(degree*16), math.ceil(degree*16)
    if ma == 16:
        ma = 15
    if mi == 16:
        mi = 15
    miS, maS = gradientC[mi], gradientC[ma]
    percentage = degree*16-mi
    return (miS[0]*percentage+maS[0]*(1-percentage), miS[1]*
            percentage+maS[1]*(1-percentage), miS[2]*percentage+maS[2]*(1-percentage))


def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1

    if n == MAX_ITER:
        return int(MAX_ITER)

    return n + 1 - log(log2(abs(z)))




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT),flags)
screen.set_alpha(None)



while not done:
    RE_START = (RE_START - coordinates[0]) * multiplier + coordinates[0]
    RE_END = (RE_END - coordinates[0]) * multiplier + coordinates[0]
    IM_START = (IM_START - coordinates[1]) * multiplier + coordinates[1]
    IM_END = (IM_END - coordinates[1]) * multiplier + coordinates[1]
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number
            c = mpc(complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START)))
            m = mandelbrot(c)
            hue = m / MAX_ITER
            screen.set_at((x, y), gradient(float(hue)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    print('Time: ',timeit.default_timer() - prev)
    prev = timeit.default_timer()
    pygame.display.flip()
    clock.tick(60)
