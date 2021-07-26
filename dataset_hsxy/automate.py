#!/usr/bin/env python3

from PIL import Image
from PIL import UnidentifiedImageError
import os

file_list=os.listdir("C:/Users/asus/Downloads/dataset/X/")
dir_path="C:/Users/asus/Downloads/dataset/result/X/"
os.makedirs(dir_path) 
print(file_list)

z=0
for x in file_list:
  try:
    im = Image.open("C:/Users/asus/Downloads/dataset/X/"+x) #file_list eachfile
  except UnidentifiedImageError:
    print("file isn't in format")

  im_rotate_new = im.resize((256,256)) #Resize the image from 3000x2000 to 600x400 pixel
    
  im_result = im_rotate_new.convert('RGB').save("C:/Users/asus/Downloads/dataset/result/X/virusx_{}.jpeg".format(z)) #Save the image to a new folder in .jpeg format

  z+=1 #counter