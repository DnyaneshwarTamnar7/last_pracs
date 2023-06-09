# -*- coding: utf-8 -*-
"""DL_2B_Practical.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O_Fx-KvtCKoaoWKVOe9pI1aMCpfPkcbE
"""

import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.datasets import imdb

(x_train,y_train),(x_test,y_test)=imdb.load_data(num_words=10000)

print("Train shape",x_train.shape)
print("Test shape",x_test.shape)

print(x_train[0])

print(y_train[0])

vocab=imdb.get_word_index()
print(vocab['ok'])

reverse_index=dict([value,key] for (key,value) in vocab.items())

reverse_index

def decode(review):
  text=""
  for i in review:
    text=text+reverse_index[i]
    text=text+" "
  return text

decode(x_train[1])

def showlen():
  print("Length of first training : ",len(x_train[0]))
  print("Length of second training sample : ",len(x_train[1]))
  print("Length of first test sample : ",len(x_test[0]))
  print("Length of second test smaple : ",len(x_test[1]))
showlen()

from keras.models import Sequential
from keras.layers import *
from tensorflow.keras.preprocessing.sequence import pad_sequences

x_train=pad_sequences(x_train,value=vocab['the'],padding='post',maxlen=256)
x_test=pad_sequences(x_test,value=vocab['the'],padding='post',maxlen=256)

decode(x_train[1])

model=Sequential()
model.add(Embedding(10000,16))
model.add(GlobalAveragePooling1D())
model.add(Dense(16,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model.fit(x_train,y_train,batch_size=128,epochs=4,verbose=1,validation_data=(x_test,y_test))

x_test[10]

y_test[10]

class_names=['Negative','Positive']

import numpy as np
predicted_value=model.predict(np.expand_dims(x_test[10],0))
print(predicted_value)
if predicted_value>0.5:
  final_value=1
else:
  final_value=0
print(final_value)
print(class_names[final_value])

loss,accuracy=model.evaluate(x_test,y_test)
print("Loss : ",loss)
print("Accuracy (Test Data) : ",accuracy*100)