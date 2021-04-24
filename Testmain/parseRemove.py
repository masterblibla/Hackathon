import lxml.etree as le

inf = 'items.xml'
outf = 'testOut.xml'

#parser (und auch bei doc) muss vorher blank text entfernen, damit pretty_print funktioniert
parser = le.XMLParser(remove_blank_text=True)


#modus 'wb' wird benötigt für pretty_print option von lxml
with open(outf, 'wb') as outfile, open(inf,'r') as infile:

    doc = le.parse(inf, parser).getroot()
    for elem in doc.xpath('//*[attribute::name]'):
        if elem.attrib['name']=='item1':
            elem.attrib.pop('name')
        else:
            parent=elem.getparent()
            parent.remove(elem)
    out = le.tostring(doc, encoding='UTF-8', xml_declaration=True, pretty_print=True)
    outfile.write(out)