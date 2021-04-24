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
    nb_children = len(root.getchildren())
    print(nb_children)

def search(eintrag, testen, ergebnis = []):
      #search(input) for testen
      for i in range(len(eintrag)):
          if eintrag[i]['tag'] == testen:
              ergebnis.append([eintrag[i]["tag"], eintrag[i]["possible_type"]])
              break
          else: 
              ergebnis = search(eintrag[i]["children"], testen)
          
      return ergebnis
        
def search_document(eintrag, testen, ergebnis = []):
    pass

#hallo André

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
                           },],
                      },],
                 },]

eg_dict_safe_list = {
    "tag": "LblPrj",
    "in_combination_with": "ProjName",
    "possible_type": "firma",
    }
#%%

if __name__ == "__main__":
    
    example_xml = '271_Test.X82'
    
    read_xml(example_xml)
    
    # eintrag = p100_tag_list
    # testen = "Descrip"
    
    # wert = search(eintrag, testen)
    # pprint.pprint(wert)
  