import sys
from PIL import Image
from random import randrange

# Pedimos un valor entre -255 y 255, este valor se le suma a cada componente del rgb de los pixeles. Si se pasa de 255, se pone 255, si vale menos de 0, se pone 0
def brillo(imagen,otra,entrada):
    rgb = imagen.convert('RGB')
    pixels = otra.load()
    brillo = entrada
    if brillo >= -255 and brillo <= 255:
        for i in range(imagen.size[0]):
            for j in range(imagen.size[1]):
                r,g,b = rgb.getpixel((i,j))
                r = r+brillo
                g = g+brillo
                b = b+brillo
                r = min(max(r,0),255)
                g = min(max(g,0),255)
                b = min(max(b,0),255)
                pixels[i,j] = (r,g,b)
        return otra
    elif brillo < -255:
        for i in range(imagen.size[0]):
            for j in range(imagen.size[1]):
                r,g,b = rgb.getpixel((i,j))
                r = 0
                g = 0
                b = 0
                pixels[i,j] = (r,g,b)
        return otra
    else:
        for i in range(imagen.size[0]):
            for j in range(imagen.size[1]):
                r,g,b = rgb.getpixel((i,j))
                r = 255
                g = 255
                b = 255
                pixels[i,j] = (r,g,b)
        return otra
