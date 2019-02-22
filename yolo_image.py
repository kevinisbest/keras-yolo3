import sys
import os
import argparse
from yolo import YOLO, detect_video
from PIL import Image

OutputPath = 'output/'
OutputTXTPath = 'outputTXT/' #for MAP

def detect_img(yolo, img_path):
    for img in os.listdir(img_path):
        print(img)
        try:
            input_image = Image.open(os.path.join(img_path,img))
        except:
            print('Open Error! Try again!')
        else:
            filename = img.split('/')[-1]
            predictname = filename.split(".")[0]+'.txt'
            file = open(OutputTXTPath+predictname,'w+')

            r_image = yolo.detect_image(input_image)
            r_image.save(OutputPath+filename)
        print('========================')
    yolo.close_session()
    
if __name__ == '__main__':
    input_path = sys.argv[1]

    print("====== Image detection mode ======")
    detect_img(YOLO(), input_path)