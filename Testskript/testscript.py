# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 18:38:48 2021

@author: andre
"""
import pprint 
import xml.etree.ElementTree as ET

def read_xml(path):
    
    tree = ET.parse(path)
    root = tree.getroot()

    return root

def analyse_xml(root):
    
    # tag_list = search_document(root)
    tag_list = [      ["City", [1,8,8]]        ]
    
    
    critical_tags_list = []
    
    for tag in tag_list:
       
    
        critical_tag = search(p100_tag_list, tag[0], location = tag[1])
        
        critical_tags_list.append(critical_tag)
    return critical_tags_list


def search(p_list, tag, location, ergebnis = [], parents = []):
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
        # parents.append(p_list[i]['tag'])
        if p_list[i]['tag'] == tag:
            ergebnis.append( {'tag': p_list[i]["tag"], 'location_xml': location, 'possible_type': p_list[i]["possible_type"]} )
           
        if p_list[i]['children'] != None: 
            ergebnis = search(p_list[i]["children"], tag, location, parents)
    
    return ergebnis



        
def search_document(eintrag, testen, ergebnis = []):
    '''
    searches document for all contained tags

    Parameters
    ----------
    eintrag : TYPE
        DESCRIPTION.
    testen : TYPE
        DESCRIPTION.
    ergebnis : TYPE, optional
        DESCRIPTION. The default is [].

    Returns
    -------
    eintrag : list
        contains all tags from xml-document.

    '''
    
    pass



#%% 
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
                          {"tag": "City",
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
    
    # example_xml = '271_Test.X82'
    # root = read_xml(example_xml)
    
    # critical_tags_list = analyse_xml(root)
    
    critical_tags_list = search(p100_tag_list,  "City", [1,8,8])
    
    pprint.pprint(critical_tags_list)
  