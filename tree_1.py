#coding: utf-8

from collections import defaultdict

def tree():
    return defaultdict(tree)

def dicts(t):
    return {k: dicts(t[k]) for k in t}

if __name__ == '__main__':
    #import json
    #users = tree()
    #users['harold']['username'] = 'hrldcpr'
    #users['handler']['username'] = 'matthand'
    #print json.dumps(users)
    taxonomy = tree()
    taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Felidae']['Felis']['cat']
    taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Felidae']['Panthera']['lion']
    taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Canidae']['Canis']['dog']
    taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Canidae']['Canis']['coyote']
    taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['tomato']
    taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['potato']
    taxonomy['Plantae']['Solanales']['Convolvulaceae']['Ipomoea']['sweet potato']
    import pprint
    pprint.pprint(dicts(taxonomy))
