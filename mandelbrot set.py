from PIL import Image, ImageDraw
from math import log, log2, floor, ceil
from collections import defaultdict
max_iter = int(input("Input the max number of iterations"))
def mandelbrot(c, z0):
    z=z0
    n=0
    while abs(z) <= 2 and n<max_iter:
        z=z*z+c
        n +=1
    if n == max_iter:
        return max_iter
    return n + 1 - log(log2(abs(z)))
def linear_interpolation(color1, color2, t):
    return color1 * (1-t) + color2 * t
Width=int(input("Input the width"))
Height=int(input("Input the height"))
re_start= -2
re_end= 1
im_start= -1
im_end= 1
julia=input("Julia sets?")
if julia == "Yes":
    real=float(input("Input the real part of c"))
    imaginary=float(input("Input the imaginary part of c"))
    c=complex(real, imaginary)
histogram = defaultdict(lambda: 0)
values={}
for x in range(0, Width):
    for y in range(0, Height):
        if julia == "Yes":
            z0= complex(re_start + (x / Width) * (re_end - re_start),
                   im_start + (y / Height) * (im_end - im_start))
        else:
            z0=0
            c=complex(re_start + (x / Width) * (re_end - re_start),
                   im_start + (y / Height) * (im_end - im_start))
        m=mandelbrot(c, z0)
        values[(x,y)]=m
        if m < max_iter:
            histogram[floor(m)] += 1
total = sum(histogram.values())
hues=[]
h=0
for i in range (max_iter):
    h += histogram[i] / total
    hues.append(h)
hues.append(h)
im=Image.new('HSV', (Width, Height), (0, 0, 0))
draw = ImageDraw.Draw(im)
for x in range(0, Width):
    for y in range(0, Height):
        m=values[(x,y)]
        hue= 255 - int(255 * linear_interpolation(hues[floor(m)], hues[ceil(m)], m%1))
        saturation=255
        value = 255 if m< max_iter else 0
        draw.point([x, y], (hue, saturation, value))
im.convert('RGB').save('output.png', 'PNG')
