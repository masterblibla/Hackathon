# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 18:38:48 2021

@author: andre
"""
import pprint 
# import xml.etree.ElementTree as ET
from lxml import etree as le

def read_xml(path):
    '''
    reads the given path into machine code

    Parameters
    ----------
    path : string
        path of geab data.

    Returns
    -------
    root : object
        root of given geab-data.

    '''
    tree = le.parse(path)
    root = tree.getroot()
    
    return root

def analyse_xml(root):
    '''
    analyse the given geab-data for critical tags, which are specified by p_lists

    Parameters
    ----------
    root : object
        root of current geab-data.

    Returns
    -------
    critical_tags_list : list
        contains all critical elements identified in the given geab-data.

    '''
    
    
    len_lxml = root.tag.rfind('}')+1
    
    tag_list = read_tags(root, root, len_lxml)
    #print("Ich bin die echte tag list", tag_list)
    
    
       
    critical_tags_list = []
    for tag in tag_list:
        critical_tag = search(p100_tag_list, tag[0], location = tag[1], ergebnis = [])
        if critical_tag != []:
            for item in critical_tag:
                critical_tags_list.append(item)
            
        
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

    Access
    -------
    ergebnis = [['tag',[possible_type1, possible_type2]]]
    '''
    
    #search(input) for tag
    for i in range(len(p_list)):
        # print('tag ins search', tag, p_list[i]['tag']) 
        
        if p_list[i]['tag'] == tag:
            ergebnis.append( {'tag': p_list[i]["tag"], 'location_xml': location, 'possible_type': p_list[i]["possible_type"]} )
            
        if p_list[i]['children'] != None: 
            ergebnis = search(p_list[i]["children"], tag, location, ergebnis)
        
    return ergebnis

   

def read_tags(root, Ebene, len_lxml, parents = [], list_of_tags = []):
    '''
    in depth search of given geab data 

    Parameters
    ----------
    root : object
        DESCRIPTION.
    Ebene : object
        current level of depth analysis.
    len_lxml : int
        length of requested lxml key.
    parents : list, optional
        contains all parents of the current Ebene. The default is [].
    list_of_tags : list, optional
        contains all information abaut tags, such as name, position. The default is [].

    Returns
    -------
    list_of_tags : list
        contains all information abaut tags, such as name, position.

    '''
    for i in range(len(Ebene)): 
        tag = Ebene[i].tag[len_lxml:]   
        parents = parents[:] + [i]
        list_of_tags.append([tag, parents])
        #('list_of_tags', list_of_tags)        #print(list_of_tags)
        if Ebene.getchildren()[i] != None:            #print(list_of_tags[-1][1])
            #print('parents: ', parents)
            read_tags(root, Ebene.getchildren()[i], len_lxml, parents, list_of_tags)
        #parents.pop(-1)
        if Ebene[i].getparent() == root:
            parents = []
        else:
            parents = [i]
    
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
                      "possible_type": ["Firmenname"],
                      "children": None,},
                     {"tag": "LblPrj",
                      "possible_type": ["Firmenname"],
                      "children": None,},
                     {"tag": "Descrip",
                      "possible_type": ["Firmenname"],
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
                           "possible_type": ["Adresse"],
                           "children": [
                               {"tag": "Name1",
                                "possible_type": ["Name"],
                                "children": None,},
                               {"tag": "Street",
                                "possible_type": ["Stra??e"],
                                "children": None,},
                               {"tag": "PCode",
                                "possible_type": ["Postleitzahl"],
                                "children": None,},
                               {"tag": "City",
                                "possible_type": ["Stadt"],
                                "children": None,},

                               ],
                           },
                  ],
                      },],
                 },]

#example of p_list entry
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
    
    
  