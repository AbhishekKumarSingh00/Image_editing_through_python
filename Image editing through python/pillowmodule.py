# installation of pillow library 
# change the image extension 
# resize image files
# resize multiple images using for loop  
# Sharpness 
# Brightess 
# Color
# Contrast 
# Image blur , GaussianBlur

from PIL import Image, ImageEnhance, ImageFilter
import os 


img1 = Image.open('Abhishek.jpeg')
img1.save('Abhi.jpg')
# img1.show()

img1 = Image.open('Abhi.jpg')
enhancer = ImageEnhance.Sharpness(img1)
enhancer.enhance(2).save('edited.jpg')

# 0 : blurry 
# 1: original image 
# 2 : image with increased sharpness 

# -------color ---------
img1 = Image.open('edited.jpg')
enhancer = ImageEnhance.Color(img1)
enhancer.enhance(1.4).save('edited.jpg')

# --------brightness -----------
img1 = Image.open('edited.jpg')
enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(1.2).save('edited.jpg')


# img1 = Image.open('edited.jpg')
# enhancer = ImageEnhance.Contrast(img1)
# enhancer.enhance(1.2).save('edited.jpg')

# image blur 

# img1.filter(ImageFilter.GaussianBlur(radius=2)).save('edited.jpg')
