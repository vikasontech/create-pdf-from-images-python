import os
from PIL import Image
import shutil
def get_file_list(path):
    return sorted(os.listdir(path))

def resize_photos(path):

    files  = get_file_list(path)

    try:
        os.mkdir("temp")
    except FileExistsError as e:
        remove_temp()
        os.mkdir("temp")
        
    for file in files:
        foo = Image.open(path+"/"+file)
        foo = foo.resize((1027,572),Image.ANTIALIAS)
        foo = foo.convert("RGB")
        foo.save("temp/"+file,optimize=True,quality=95)

    return "temp"
        
def remove_temp():
    shutil.rmtree('temp') 
