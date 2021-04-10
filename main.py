import io
import pandas as pd
import string
import logging

logging.basicConfig(filename='data.log', level=logging.DEBUG)

def remove_unwanted(s):
    return s.translate(str.maketrans('', '', string.punctuation))

# Create .csv with all the words indexed in it
df_all = {'word': [], 'position': []}
f = io.open("data/book/hpmor.txt", mode="r", encoding="utf-8")
f = f.read()
i = 0
logging.info("Creating dataframe containing all the words in the book: ")
for word in f.split():
    word = remove_unwanted(word)
    if not len(word) == 0:
        df_all['word'].append(word)
        df_all['position'].append(i)
    i += 1

logging.info("Exporting dataframe to csv: ")
df_all = pd.DataFrame(data=df_all)
df_all.to_csv('data/data.csv', index=False)

# Create .csv with the character names indexed in it
charlist_lower = ['hannah abbott', 'amelia bones', 'susan bones', 'lavender brown', 'bellatrix black', 'penelope clearwater', 'albus dumbledore', 'dudley dursley', 'vernon dursley', 'petunia evansverres', 'fawkes', 'filius flitwick', 'hermione granger', 'daphne greengrass', 'neville longbottom', 'draco malfoy', 'lucius malfoy', 'narcissa malfoy', 'minerva mcgonagall', 'madeye moody', 'theodore nott', 'padma patil', 'parvati patil', 'peter pettigrew', 'harry potter', 'james potter', 'lily potter', 'quirinius quirrell', 'tom riddle', 'rita skeeter', 'sybill trelawney', 'voldemort', 'ron weasley', 'blaise zabini', 'george weasley', 'fred weasley', 'molley weasley', 'arthur weasley']
charlist_split_lower = ['hannah', 'abbott', 'amelia', 'bones', 'susan', 'bones', 'lavender', 'brown', 'bellatrix', 'black', 'penelope', 'clearwater', 'albus', 'dumbledore', 'dudley', 'dursley', 'vernon', 'dursley', 'petunia', 'evansverres', 'fawkes', 'filius', 'flitwick', 'hermione', 'granger', 'daphne', 'greengrass', 'neville', 'longbottom', 'draco', 'malfoy', 'lucius', 'malfoy', 'narcissa', 'malfoy', 'minerva', 'mcgonagall', 'mad-eye', 'moody', 'theodore', 'nott', 'padma', 'patil', 'parvati', 'patil', 'peter', 'pettigrew', 'harry', 'potter', 'james', 'potter', 'lily', 'potter', 'quirinius', 'quirrell', 'tom', 'riddle', 'rita', 'skeeter', 'sybill', 'trelawney', 'voldemort', 'ron', 'weasley', 'blaise', 'zabini', 'george', 'weasley', 'fred', 'weasley', 'molley', 'weasley', 'arthur', 'weasley']

df_chars = {'name': [], 'position': []}
f = io.open("data/book/hpmor.txt", mode="r", encoding="utf-8")
f = f.read()
i = 0
f = f.split()
logging.info("Creating dataframe containing all the names in the book: ")

def get_full_name(word):
    for e in charlist_lower:
        if word in e:
            return e

read_name = False
for index, word in enumerate(f):
    if read_name:
        i += 1
        read_name = False
        continue
    try:
        if len(word) > 3:
            word = remove_unwanted(word).lower()
            nextword = remove_unwanted(f[index+1]).lower()

            if word+" "+nextword in charlist_lower: # or word+"s" in charlist_split_lower: for names like harrys and hermiones
                df_chars['name'].append(word+" "+nextword)
                df_chars['position'].append(i)
                read_name = True
            elif word in charlist_split_lower: # or word+"s" in charlist_split_lower: for names like harrys and hermiones
                df_chars['name'].append(get_full_name(word))
                df_chars['position'].append(i)
    except Exception as e:
        pass

    i += 1

logging.info("Exporting dataframe to csv: ")
df_all = pd.DataFrame(data=df_chars)
df_all.to_csv('data/data_chars.csv', index=False)