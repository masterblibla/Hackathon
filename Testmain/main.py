import sys, os
import xml.etree.ElementTree as ET
import lxml.etree as le

#path = 'C:\\Users\\YvesGeib\\GAEB\\Hochbau\\GAEB DA XML'
#path = os.getcwd()
#filename = '0131.X84'
#tree = ET.parse(os.path.join(path, filename))
#root = tree.getroot()
# get criticaltags, type of criticaltag (name, address)



"""
get criticaltags with location
jump to criticaltags in document
replace current criticaltag with anonymous tag (blacken or "Musterstrasse")
"""

"""
example dictionary:
[{'tag': "City", 'location': [0,1,8], 'type': [pos_type1, pos_type2]},
 {'tag': "City", 'location': [0,1,8], 'type': [pos_type1, pos_type2]},
 {'tag': "City", 'location': [0,1,8], 'type': [pos_type1, pos_type2]}]
"""

#parser (und auch bei doc) muss vorher blank text entfernen, damit pretty_print funktioniert


#criticaltag = 'item'
#taglocation = root[0][0]



"""
gets an XML file and produces a dictionary containing information about the tag

@param inf: XML file
@param outf: refactored XML file for testing purposes
@rtype: dict
@returns: a dictionary with three elements {'tag', 'location', 'tagtype'}
"""

def parseFile(inf, outf):
    parser = le.XMLParser(remove_blank_text=True)



    with open(outf, 'wb') as outfile, open(inf,'r') as infile:
        root = le.parse(infile, parser).getroot()

        #out = le.tostring(root, encoding='UTF-8', xml_declaration=True, pretty_print=True)
        #outfile.write(out)

    taginfo = {'tag': 'blub', 'location': [0, 1, 0], 'type': 'name'}
    return taginfo


"""
gets a taginfo dictionary and anonymizes the contained text (refactors by blackening)

@type taginfo: dict
@param taginfo: a dictionary with three elements {'tag', 'location', 'tagtype'}
@returns: an XML file with redacted content
"""
def blackenTagText(location):

    #get number of elements in location list and translate it into full location

    locationlist = taginfo['location']
    location = recursefunc(root, locationlist)
    #root[0][1]
    #failsafe whether tag is correct and really exists at this point
    if taginfo['tag'] != location.tag:
        raise Exception("The tags don't match, anonymizing stopped. Please restart application.")
    else:
        print(location.text)

"""
takes a root and a list of numbers and returns the location of the tag at those children
corresponding to the numbers, starting from root
It has to appended with they XML type at the end, for example print(recursefunc(root, location).tag)

@param root: an XML tree at the root
@param location: a list of numbers
@returns: the tag at the required location, starting from root
"""
def recursefunc(root, location):

    rootNew = root[location[0]]
    pop = location.pop(0)
    if location != []:
        rootNew = recursefunc(rootNew, location)

    return rootNew



if __name__ == '__main__':
    inf = 'items.xml'
    outf = 'testOut.xml'

    parser = le.XMLParser(remove_blank_text=True)
    root = le.parse(inf, parser).getroot()
    taginfo = parseFile(inf, outf)
    blackenTagText(taginfo)

