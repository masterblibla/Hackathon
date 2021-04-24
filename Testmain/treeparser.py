# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
# Konzeptidee:
"""
dict = {'strasse': 'Musterstrasse',
        'name': 'Max Mustermann'}
if dict('strasse'):
    return dict.get('strasse')
if dict('name'):
    return dict.get('name')
"""

print(os.getcwd())

import xml.etree.ElementTree as ET
tree = ET.parse('items.xml')
root = tree.getroot()

#one specific item attribute
print('Item #2 attribute:')
print(root[0][1].attrib)

#TODO: Is nesting once enough?
#all item attributes
print('\nAll attributes:')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)

#one specific item data
print('\nItem #2 ata')
print('Item #2 attribute: ')
print(root[0][1].text)

#all item data
print('\nAl item data:')
for elem in root:
    for subelem in elem:
        print(subelem.text)

print('\nitem count: ' + str(len(root[0])))

"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
