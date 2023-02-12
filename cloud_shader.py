import math
import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


# Ваш код здесь:
def func(x, y):
    a = value_noise(x,y,4)
    a += value_noise(x,y,8)*0.5
    a += value_noise(x,y,16)*0.25
    a += value_noise(x,y,32)*0.125
    a += value_noise(x,y,64)*0.0625
    a/=1.8
    return a, a/2+0.5, 1

def value_noise_y(x,y,size):
    
    yr = y*size//1/size
    dy = (1/size) -(y- yr)
    dy = (1 - dy*size)
    dy = dy*dy*(3-2*dy)
    
    a = noise(x,y,size)
    b = noise(x,y-1/size,size)
    r = lerp(a,b,dy)
    return r

def value_noise(x,y,size):
    xr = x*size//1/size
    dx = (1/size) -(x- xr)
    dx = (1 - dx*size)
    dx = dx*dx*(3-2*dx)

    a = value_noise_y(x,y,size)
    b = value_noise_y(x-1/size,y,size)
    r = lerp(a,b,dx)
    return r


def noise(x,y,size):
    x = x*size//1/size
    y = y*size//1/size
    rand = x*1009983 + y*y*6327
    rand *= rand * rand
    rand = (math.sin(rand) + 1)/2
    return rand

def lerp(a,b,c):
    return (c * a) + ((1-c) * b)

label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
