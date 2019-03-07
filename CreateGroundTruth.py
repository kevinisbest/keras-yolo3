import xml.etree.ElementTree as ET
import os

xml_path = 'D:/data/Images_xml' # all xml path
txt_path = 'D:/data/Images_txt' # all txt output path
dirs = os.listdir(xml_path)       # read all file in dir
for file in sorted(dirs):
    xml_name = file.split('.')[0]
    in_file = open(xml_path + '/' + file)
    tree = ET.parse(in_file)
    root = tree.getroot()
    txt_file = open(txt_path+ '/' + xml_name +'.txt',"w+")
    for obj in root.findall('object'):
        class_name = obj.find('name').text     # get class name
        
        xmlbox = obj.find('bndbox')          # get bounind box
        border = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text),
                  int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        txt_file.write('%s %d %d %d %d\n' %(class_name,border[0],border[1],border[2],border[3]))
    txt_file.close()