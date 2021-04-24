import pprint
import lxml.etree as le
import tag_script as ts
import logging

#path = 'C:\\Users\\YvesGeib\\GAEB\\Hochbau\\GAEB DA XML'
#path = os.getcwd()
#filename = '0131.X84'
#tree = ET.parse(os.path.join(path, filename))
#root = tree.getroot()
logfile = 'logfile.txt'

logging.basicConfig(filename=logfile,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)



logger = logging.getLogger('anonymizingLogger')


"""
get criticaltags with location
jump to criticaltags in document
replace current criticaltag with anonymous tag (blacken or "Musterstrasse")

example dictionary:
[{'tag': "City", 'location': [0,1,8], 'type': [pos_type1, pos_type2]},
 {'tag': "City", 'location': [0,1,8], 'type': [pos_type1, pos_type2]},
 {'tag': "City", 'location': [0,1,8], 'type': [pos_type1, pos_type2]}]
"""

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
gets a list of taginfo dictionaries and anonymizes the contained text (refactors by blackening)

@type taginfo: dict
@param taginfo: a dictionary with three elements {'tag', 'location', 'tagtype'}
@returns: an XML file with redacted content
"""
def blackenTagText(critical_tags_list, root):
    # One print to rule them all
    print('critical_tags_list: ', critical_tags_list)

    # Loop over the critical tags and anonymize each one
    for elem in critical_tags_list:
        # saving location to update logger. Gets removed in recursefunction with pop()
        logger.info(str(('Current location starting from root going through the children', elem['location_xml'])))

        # Process input dict and get the location element in current xml document
        # WARNING: location content gets deleted during recursefunc
        location = recursefunc(root, elem['location_xml'])

        # failsafe if tag is correct and really exists at this point
        if elem['tag'] != location.tag:
            logger.info('The tags don\'t match, anonymizing stopped.')
            raise Exception('The tags don\'t match, anonymizing stopped. Please restart application.')
        # Another failsafe if tag contains text
        elif location.text == None:
            logger.info('This element does not contain text.')
            raise Exception('This element does not contain text.')
        # Replace private text content with anonymized text
        else:
            logger.info('changed current text \"' + location.text + '\" of tag ' + location.tag)
            location.text = 'anonymized text'
            logger.info('into \"' + location.text + '\"')
            logger.info('Anonymizing for tag ' + location.tag + ' completed.\n')


    # Output of xml to new file testOut.xml
    outf = 'testOut.xml'
    with open(outf, 'wb') as outfile:
        out = le.tostring(root, encoding='UTF-8', xml_declaration=False, pretty_print=True)
        outfile.write(out)




"""
takes a root and a list of numbers and returns the location of the tag at those children
corresponding to the numbers, starting from root
It has to appended with they XML type at the end, for example print(recursefunc(root, location).tag)

@param root: an XML tree at the root
@param location: a list of numbers
@returns: the element at the required location, starting from root. To get tag, one needs to add rootNew.tag
@returns: also the location list
"""
def recursefunc(root, location):

    rootNew = root[location[0]]
    location.pop(0)
    if location != []:
        rootNew = recursefunc(rootNew, location)

    return rootNew



if __name__ == '__main__':

    example_xml = 'items.xml'
    root = ts.read_xml(example_xml)
    critical_tags_list = ts.analyse_xml(root)
    pprint.pprint('--------------------------')
    pprint.pprint(critical_tags_list)

    blackenTagText(critical_tags_list, root)
    #parser = le.XMLParser(remove_blank_text=True)
    #root = le.parse(inf, parser).getroot()
    #taginfo = parseFile(inf, outf)
    #blackenTagText(taginfo)
    
    

