#python3.8
import spacy
from spacy.lang.es.examples import sentences 
from spacy.lang.en import English
nlp_english = spacy.load('en_core_web_sm')
nlp_spanish = spacy.load('es_core_web_sm')

#nlp_english = en_core_news_sm.load()
english_doc = nlp_english("Mexico is a country in the southern portion of North America. It is bordered to the north by the United States; to the south and west by the Pacific Ocean; to the southeast by Guatemala, Belize, and the Caribbean Sea; and to the east by the Gulf of Mexico")
spanish_doc = nlp_spanish("México es un país en la parte sur de América del Norte. Limita al norte con los Estados Unidos; al sur y al oeste por el Océano Pacífico; al sureste con Guatemala, Belice y el Mar Caribe; y al este por el Golfo de México")
#print([(w.text, w.pos_) for w in doc])

spanish_nouns = [w.text for w in spanish_doc if w.pos_ == 'NOUN']
english_nouns = [w.text for w in english_doc if w.pos_ == 'NOUN']

cognates = []


#this function will take a lot of editing and heuristics
def find_noun_with_min_edit_distance(noun, english_nouns):
  if noun_length == 0:
    return english_nouns_length
  if english_nouns_length == 0:
    return noun_length
  if noun[noun_length-1] == english_noun[english_nouns_length-1]:
    return editDistance(noun, english_noun, noun_length-1, english_nouns_length-1)
  return 1 + min(editDistance(noun, english_noun, noun_length, english_nouns_length-1),    # Insert
                   editDistance(noun, english_noun, noun_length-1, english_nouns_length),    # Remove
                   editDistance(noun, english_noun, noun_length-1, english_nouns_length-1)    # Replace
                   )
  #this returns how far words are apart from eachother
  #but I should give weight to some letters, like how é is closer to e than t



for noun in spanish_nouns:
  cognate[noun] = find_noun_with_min_edit_distance(noun, english_nouns, noun_length, englishs_noun_length)
  print('this works')
