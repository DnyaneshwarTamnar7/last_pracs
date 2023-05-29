import pandas as pd
import numpy as np

train_df=pd.read_csv("Google_Stock_Price_Train.csv")

train_df

test_df=pd.read_csv("Google_Stock_Price_Test.csv")

test_df

test_df.info()

from sklearn.preprocessing import MinMaxScaler

train_df['Close']=train_df['Close'].astype(str).str.replace(",","").astype(float)
test_df['Close']=test_df['Close'].astype(str).str.replace(",","").astype(float)

train_scaler=MinMaxScaler()
train_df['Normalized Close']=train_scaler.fit_transform(train_df['Close'].values.reshape(-1,1))

test_scaler=MinMaxScaler()
test_df['Normalized Close']=test_scaler.fit_transform(test_df['Close'].values.reshape(-1,1))

x_train=train_df['Normalized Close'].values[:-1].reshape(-1,1,1)
y_train=train_df['Normalized Close'].values[1:].reshape(-1,1,1)

x_test=test_df['Normalized Close'].values[:-1].reshape(-1,1,1)
y_test=test_df['Normalized Close'].values[1:].reshape(-1,1,1)

print("X_train shape:",x_train.shape)
print("y_train shape:",y_train.shape)
print("x_test shape:",x_test.shape)
print("y_test shape:",y_test.shape)

from keras.models import Sequential
from keras.layers import LSTM,Dense

model=Sequential()
model.add(LSTM(4,input_shape=(1,1)))
model.add(Dense(1))
model.compile(loss="mean_squared_error",optimizer='adam')
model.summary()

model.fit(x_train,y_train,epochs=100,batch_size=1,verbose=1)

y_pred=model.predict(x_test)

y_test_actual = test_scaler.inverse_transform(y_test.reshape(-1, 1))
y_pred_actual = test_scaler.inverse_transform(y_pred.reshape(-1, 1))

print("Actual value:{:.2f}".format(y_test_actual[1][0]))
print("Predicted value:{:.2f}".format(y_pred_actual[1][0]))