from pytesser import *
from PIL import Image

im = Image.open('phototest.tif')
text = image_to_string(im)
print text