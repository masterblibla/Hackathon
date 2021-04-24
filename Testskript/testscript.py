# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 18:38:48 2021

@author: andre
"""
import pprint 
import xml.etree.ElementTree as ET
from lxml import etree

def read_xml(path):
    
    tree = ET.parse(path)
    root = tree.getroot()
    
    return root

def analyse_xml(root):
    
    
    len_lxml = root.tag.rfind('}')+1
    
    tag_list = read_tags(root, len_lxml)
    
    
   
       
    critical_tags_list = []
    for tag in tag_list:
        print(tag[0])
        critical_tag = search(p100_tag_list, tag[0], location = tag[1], ergebnis = [])
        if critical_tag != []:
            critical_tags_list.append(critical_tag)
            
        
    return critical_tags_list


def search(p_list, tag, location, ergebnis = []):
    '''
    recursive in depth search of defined critical tags

    Parameters
    ----------
    p_list : list
        list containing the user defnined critical tags.
    tag : string
        string that needs to be checked. 
    ergebnis : list, optional
        contains informatioon, if the tag matches one of the critical tags. The default is [].

    Returns
    -------
    ergebnis : list
        contains all matched critical tags and posssible data-types.

    Acces
    -------
    ergebnis = [['tag',[possible_type1, possible_type2]]]
    '''
    
    #search(input) for tag
    for i in range(len(p_list)):
        print('tag ins search', tag, p_list[i]['tag']) 
        
        if p_list[i]['tag'] == tag:
            ergebnis.append( {'tag': p_list[i]["tag"], 'location_xml': location, 'possible_type': p_list[i]["possible_type"]} )
            
        if p_list[i]['children'] != None: 
            ergebnis = search(p_list[i]["children"], tag, location, ergebnis)
        
    return ergebnis



        

        
# def read_tags(Ebene, len_lxml, parents = [], list_of_tags = [] ):
#    for i in range(len(Ebene)):
       
#        list_of_tags.append([Ebene[i].tag[len_lxml:], parents])
#        parents.append(Ebene[i].tag[len_lxml:]) 
#        #print(parents)
#        if Ebene.getchildren()[i] != None:
#            list_of_tags = read_tags(Ebene.getchildren()[i], len_lxml, [parents])
         
         # parents.append(Ebene[i].tag[len_lxml:])   
#        parents = []    
#    return list_of_tags
    

def read_tags(Ebene, len_lxml, parents = [], list_of_tags = []):

    for i in range(len(Ebene)):

        tag = Ebene[i].tag[len_lxml:]



        parents = parents[:] + [i]
        list_of_tags.append([tag, parents])
        print('list_of_tags', list_of_tags)


        #print(list_of_tags)
        if Ebene.getchildren()[i] != None:
            list_of_tags[-1][1] = parents
            #print('list of tags', list_of_tags)
            print('parents: ', parents)
            read_tags(Ebene.getchildren()[i], len_lxml, parents, list_of_tags)
        #parents.pop(-1)
            #print(list_of_tags)
        parents = [i]






    #list_of_tags[]

    #print(list_of_tags)

   #[['items', 0], ['item', 00], ['blub', 000], ['item', 0001], ['blub', 00010], ['deeperblub', 000100], ['seconditems', 1],
    #['blubitem', 10]]
    return list_of_tags
    
    
#%% p Lists
#tags which dont contain dsgvo
p00_tag_list = [""]

#tags which contain dsgvo with 50 Percent
p50_tag_list = [
                {"tag": "PrjInfo",
                 "possible_type": None,
                 "children": [
                     {"tag": "NamePrj",
                      "possible_type": ["Firmename"],
                      "children": None,},
                     {"tag": "LblPrj",
                      "possible_type": ["Firmenname"],
                      "children": None,},
                     {"tag": "Descrip",
                      "possible_type": ["Firmename"],
                      "children": None,},
                                ],
                    },]

#tags which contain dsgvo with 100 Percent
p100_tag_list = [
                {"tag": "Award",
                 "possible_type": None,
                 "children": [
                     {"tag": "CTR",
                      "possible_type": ["Firmenname"],
                      "children": [
                          {"tag": "Address",
                           "possible_type": ["Addresse"],
                           "children": [
                               {"tag": "Name1",
                                "possible_type": ["Name"],
                                "children": None,},
                               {"tag": "Street",
                                "possible_type": ["Straße"],
                                "children": None,},
                               {"tag": "PCode",
                                "possible_type": ["Postleitzahl"],
                                "children": None,},
                               {"tag": "City",
                                "possible_type": ["Stadt"],
                                "children": None,},
                               
                               ],
                           },
                          {"tag": "item",
                           "possible_type": ["Addresse"],
                           "children": [
                               {"tag": "Name1",
                                "possible_type": ["Name"],
                                "children": None,},
                               {"tag": "Street",
                                "possible_type": ["Straße"],
                                "children": None,},
                               {"tag": "PCode",
                                "possible_type": ["Postleitzahl"],
                                "children": None,},
                               {"tag": "City",
                                "possible_type": ["Gebäudename"],
                                "children": None,},
                               
                               ],
                           },],
                      },],
                 },]

# eg_dict_safe_list = {
#     "tag": "LblPrj",
#     "possible_type": "firma",
#     "children": [...]
#     }
#%%

if __name__ == "__main__":
    
    example_xml = 'items.xml'
    root = read_xml(example_xml)
  
    critical_tags_list = analyse_xml(root)
    pprint.pprint('--------------------------')
    pprint.pprint(critical_tags_list) 
    
  