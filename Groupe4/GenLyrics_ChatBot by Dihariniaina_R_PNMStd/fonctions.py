import numpy as np #le calcul scientifique en Python
import tensorflow as tf #pour construire et entraîner des modèles de réseaux de neurones, ainsi que pour effectuer des opérations mathématiques sur des tenseurs.
import pandas as pd #pour l'analyse de données en Python.

from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding , LSTM , Bidirectional , Dropout

#Relier les données avec la fonction Python
filepath="data/tononkira4.csv"

#Importation des données avec Pandas

df = pd.read_csv(filepath)

#Voir qui est le c
df.Mpihira.value_counts()

corpus = np.array(df[df.Mpihira=="Mahaleo"].Tononkira)

#Preprocessing
# cleaning up the lyrics
corpus = '\n'.join([x.lower() for x in corpus])       # join all songs to form on big corpus
corpus = corpus.split('\n')                           # split the lines
corpus = [x for x in corpus if not x.startswith('//www')]
corpus = [x for x in corpus if not x.startswith('[')] # removing comments starting with [
corpus = [x for x in corpus if x != '']               # removing empty items
corpus = [x.replace("\r","") for x in corpus if x != '']

#Data encoding using a tokenizer algorithm
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
word_index = tokenizer.word_index
reverse_word_index = dict([(v,k) for (k,v) in word_index.items()])

TOTAL_WORDS = len(word_index) + 1
print ('Total words in all Mahaleo songs:', TOTAL_WORDS) # added 1 for OOV token

input_sequences = []
for line in corpus:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_seq = token_list[:i+1]
        input_sequences.append(n_gram_seq)

MAX_SEQ_LEN = max([len(x) for x in input_sequences])
print ('Max Sequence Length :', MAX_SEQ_LEN)

#Transformation des donées en numpy matrux pour etre un NNM
input_sequences = np.array(pad_sequences(input_sequences, maxlen = MAX_SEQ_LEN, padding = 'pre'))
xs = input_sequences[:,:-1]
labels = input_sequences[:,-1]
ys = tf.keras.utils.to_categorical(labels, num_classes = TOTAL_WORDS)
xs.shape, ys.shape

#Conceptiond de la model d'architecture
# improve the model performance by adjusting these hyperparameters
EPOCH_SIZE=500  # this is the number of times the model will be trained
BATCH_SIZE=256   # this is the sampling size of data for each training epoch

#Here we set all the parameters and hyperparameters of the LSTM model.
#The LSTM model here has the architect of 5 layers ( 1 Embedding layer , 2 bidirectional layers , 1 dropout layer and a  dense layer )

# Initinializing the neural network model
model = Sequential([
    Embedding(TOTAL_WORDS, 256, input_length = MAX_SEQ_LEN - 1),
    Bidirectional(LSTM(64, return_sequences = True)),
    Bidirectional(LSTM(64)),
    Dropout(0.2),
    Dense(TOTAL_WORDS, activation = 'softmax')
])

model.compile(loss = 'categorical_crossentropy', metrics = ['accuracy'], optimizer = 'adam')
model.summary()

# Model training
history = model.fit(xs, ys, epochs = EPOCH_SIZE, verbose = 2, batch_size = BATCH_SIZE)

#Test 
"""def generate_lyrics(text_input,n_words):
    Input Parameters :
         - text_input (string): The word to begin the lyrics
         - n_words (integer) : the number of words the model will generate beginning with text_input

      Output :
         text_output (string) : the text input + generated words

  
  seed_text=text_input
  for _ in range(n_words):
      token_list = tokenizer.texts_to_sequences([seed_text])[0]
      token_list = pad_sequences([token_list], maxlen = MAX_SEQ_LEN - 1, padding = 'pre')
      predicted = model.predict(token_list,verbose=0)
      classes_x=np.argmax(predicted,axis=1)
      seed_text += ' ' + reverse_word_index[classes_x[0]]
  text_output=seed_text
  return text_output"""

def generate_lyrics(text_input):
    """ Input Parameters :
           - text_input (string): The word to begin the lyrics

        Output :
           text_output (string) : the text input + generated paragraph of lyrics
    """
    n_words = 16  # Nombre de mots à générer
    seed_text = text_input

    for _ in range(n_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=MAX_SEQ_LEN - 1, padding='pre')
        predicted = model.predict(token_list, verbose=0)
        classes_x = np.argmax(predicted, axis=1)
        seed_text += ' ' + reverse_word_index[classes_x[0]]

    text_output = seed_text + '\n'
    return text_output 

  # Example of use of the generate_lyrics function
# inpired by Mahaleo lyrics
#print(generate_lyrics('Miverena',4))
#print(generate_lyrics('Anefa',4))
#print(generate_lyrics('Malahelo',4))
#print(generate_lyrics('Aza',4))

