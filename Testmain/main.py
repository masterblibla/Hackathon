import sys, os
import xml.etree.ElementTree as ET

#path = 'C:\\Users\\YvesGeib\\GAEB\\Hochbau\\GAEB DA XML'
path = os.getcwd()
filename = '0131.X84'
tree = ET.parse(os.path.join(path, filename))
root = tree.getroot()

for elem in root:
    for subelem in elem:
        for subsubelem in subelem:
            print(subsubelem.text)