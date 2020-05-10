import os
from fpdf import FPDF
import resize_image as rp 


pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
#pdf_file_name="sample_demo_new_2.pdf"

def get_file_list(path):
    return sorted(os.listdir(path))


def add_image(image_path):
    ydiff = 52
    pdf.image(image_path, x=5, y=8, w=90)
    pdf.image(image_path, x=105, y=8, w=90)
    pdf.image(image_path, x=5, y=60, w=90)
    pdf.image(image_path, x=105, y=60, w=90)
    pdf.image(image_path, x=5, y=60+ydiff, w=90)
    pdf.image(image_path, x=105, y=60+ydiff, w=90)


    pdf.image(image_path, x=5, y=112+ydiff, w=90)
    pdf.image(image_path, x=105, y=112+ydiff, w=90)
    pdf.image(image_path, x=5, y=164+ydiff, w=90)
    pdf.image(image_path, x=105, y=164+ydiff, w=90)



def create_pdf(path):

    print("resizing photos...")

    #resize photos
    try:
        new_path = rp.resize_photos(path)
    except FileNotFoundError as e:
        print(f"file path '{path}' not found in system")
        exit()

    print(f"creating pdf {pdf_file_name} ...")
    row_limit = 5
    r = 0
    y = 8
    x = 5
    i = 0 

    files = get_file_list(new_path)

    for file in files:

       i = i + 1

       if(i % 2==0):
           x = 105
       else:
           x = 5

       if(r >= row_limit):
           r = 0
           y = 8
           pdf.add_page()

       #print(f"r: {r} x: {x}, y: {y}:: file: {file}")
       pdf.image(new_path+"/"+file, x=x, y=y, w=90)

       if(i%2==0):
           y = y + 52
           r = r + 1

    try:
        pdf.output(pdf_file_name)
    except FileNotFoundError as  e: 
        print(f"Invalid file name:{pdf_file_name} ")

    rp.remove_temp()

path = input("Input the image path that have image files: ")
#path = "/Users/vikas/Documents/aws"

pdf_file_name=input("Destination file name and path: ")

create_pdf(path)


