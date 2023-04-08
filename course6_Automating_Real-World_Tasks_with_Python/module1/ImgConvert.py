import os
from PIL import Image
import imghdr

img_source_path = ""
img_target_path = ""

def convert_img(img_file):
    img = Image.open(img_source_path+img_file)
    new_img = img.rotate(90).resize((128,128)).convert("RGB")
    new_img.save(img_target_path + img_file+".jpeg")



if __name__ == "__main__":
    for img_file in os.listdir(img_source_path):
        if imghdr.what(img_source_path+img_file) == "tiff":
            convert_img(img_file)
            print(img_file + " processed \n")
        else:
            print(img_file + " is not a tiff file \n")
        
        