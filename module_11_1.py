import requests as req
import numpy as np
from PIL import Image, ImageOps


r = req.get('https://api.github.com/events')
print(r.json())
print(r.content)
print(r.headers)

a = np.array([['1.1', '1.1'],['1.1', '1.1'],['1.1', '1.1']])
b = np.ones((3,2))
c = a.astype('float')
print('a\n', a)
print('b\n', b)
print('c\n', c)

im = Image.open('./2.jpg')
print(im.format, im.size, im.mode)
ImageOps.cover(im, (1200, 900)).save('imageops_cover.webp')
im2 = Image.open('./imageops_cover.webp')
print(im2.format, im2.size, im2.mode)