#python3.8
import spacy
nlp_english = spacy.load('en_core_web_sm')
from spacy.lang.en import English
#nlp_english = en_core_news_sm.load()
english_doc = nlp_english("Mexico is a country in the southern portion of North America. It is bordered to the north by the United States; to the south and west by the Pacific Ocean; to the southeast by Guatemala, Belize, and the Caribbean Sea; and to the east by the Gulf of Mexico")
spanish_doc = nlp_spanish("México es un país en la parte sur de América del Norte. Limita al norte con los Estados Unidos; al sur y al oeste por el Océano Pacífico; al sureste con Guatemala, Belice y el Mar Caribe; y al este por el Golfo de México")
#print([(w.text, w.pos_) for w in doc])

spanish_nouns = [w.text for w in spanish_doc if w.pos_ == 'NOUN']
english_nouns = [w.text for w in english_doc if w.pos_ == 'NOUN']

cognates = []

for noun in spanish_nouns:
  cognate[noun] = find_noun_with_min_edit_distance(noun, english_nouns)

'''
this function will take a lot of editing
def find_noun_with_min_edit_distance():

'''