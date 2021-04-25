import pprint
import lxml.etree as le
import tag_script as ts
import logging
import os

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



logger = logging.getLogger('AnonLogger')


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
def blackenTagText(critical_tags_list, root, path):
    # One print to rule them all
    print('critical_tags_list: ', critical_tags_list)
    # Omit unnecessary content like https
    len_lxml = root.tag.rfind('}') + 1

    # Loop over the critical tags and anonymize each one
    for elem in critical_tags_list:
        # saving location to update logger. Gets removed in recursefunction with pop()
        logger.info(str(('Current location starting from root going through the children', elem['location_xml'])))

        # Process input dict and get the location element in current xml document
        # WARNING: location content gets deleted during recursefunc
        location = recursefunc(root, elem['location_xml'])
        #location =
        print('location:', location.tag[len_lxml:])
        print(elem['tag'])
        # failsafe if tag is not correct and does not exist at this point
        if elem['tag'] != location.tag[len_lxml:]:
            logger.info('The tags don\'t match, anonymization stopped.\n')
            raise Exception('The tags don\'t match, anonymization stopped. Please restart application.')
        # Another failsafe if tag does not contain text
        elif location.text == None:
            location.text = ''
            logger.info('This element does not contain text. Anonymization skipped.\n')
            #continue
            #raise Exception('This element does not contain text.')

        # Replace private text content with anonymized text
        else:
            print('elem: ', elem)
            if elem['possible_type'] == None:
                logger.info('changed current text \"' + location.text + '\" of tag ' + location.tag[len_lxml:])
                location.text = 'XXXX'
                logger.info('into \"' + location.text + '\"')
            elif 'Name' in elem['possible_type']:
                logger.info('changed current text \"' + location.text + '\" of tag ' + location.tag[len_lxml:])
                location.text = 'Mustermann/Musterfrau'
                logger.info('into \"' + location.text + '\"')
            elif 'Straße' in elem['possible_type']:
                logger.info('changed current text \"' + location.text + '\" of tag ' + location.tag[len_lxml:])
                location.text = 'Musterstraße'
                logger.info('into \"' + location.text + '\"')
            elif 'Postleitzahl' in elem['possible_type']:
                logger.info('changed current text \"' + location.text + '\" of tag ' + location.tag[len_lxml:])
                location.text = '65432'
                logger.info('into \"' + location.text + '\"')
            elif 'Stadt' in elem['possible_type']:
                logger.info('changed current text \"' + location.text + '\" of tag ' + location.tag[len_lxml:])
                location.text = 'Musterstadt'
                logger.info('into \"' + location.text + '\"')
            elif 'Adresse' in elem['possible_type']:
                logger.info('changed current text \"' + location.text + '\" of tag ' + location.tag[len_lxml:])
                location.text = 'Musteradresse'
                logger.info('into \"' + location.text + '\"')
            """
            logger.info('changed current text \"' + location.text + '\" of tag ' + location.tag[len_lxml:])
            location.text = 'Musteradresse'
            logger.info('into \"' + location.text + '\"')
            """
            logger.info('Anonymizing for tag ' + location.tag[len_lxml:] + ' completed.\n')

    # Get extension of input file

    # Output of xml to new file. Filename added with _Anon
    #for fp in path:
        #filename = os.path.splitext(fp)[0]
        #ext = os.path.splitext(fp)[-1]
        #outf = fp + '_Anon' + ext

    outf = 'ANON_' + path
    print(outf)
    with open(outf, 'wb') as outfile:
        out = le.tostring(root, encoding='UTF-8', xml_declaration=True, pretty_print=True)
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

    # TODO: path = list of files
    path = '271_Test.X82'
    example_xml = 'items.xml'
    root = ts.read_xml(path)
    critical_tags_list = ts.analyse_xml(root)
    pprint.pprint('--------------------------')
    pprint.pprint(critical_tags_list)

    blackenTagText(critical_tags_list, root, path)
    #parser = le.XMLParser(remove_blank_text=True)
    #root = le.parse(inf, parser).getroot()
    #taginfo = parseFile(inf, outf)
    #blackenTagText(taginfo)
    
    

