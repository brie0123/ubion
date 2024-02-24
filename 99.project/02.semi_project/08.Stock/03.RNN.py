from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
import numpy as np
# import matplotlip.pyplot as plt
import analyzer

mk = analyzer.MarketDB()
raw_df = mk.get_daily_price('000020','2021-01-15','2023-01-15')

window_size = 10
data_size = 4

def MinMaxScaler(data):
    numerator = data - np.min(data,0)
    denominator = np.max(data,0) - np.min(data,0)
    return numerator / denominator + 1e-7

dfx = raw_df[['open','high','low','close']]
dfx = MinMaxScaler(dfx)
dfy = dfx[['close']]

x = dfx.values.tolist()
y = dfy.values.tolist()

print(dfx, dfy)

data_x = []
data_y = []


for i in range(len(y) - window_size):
    _x = x[i: i + window_size]
    _y = y[i + window_size]
    data_x.append(_x)
    data_y.append(_y)
    # print(_x, "-"),_y
    
train_size = int(len(data_y) * 0.7)
train_x = np.array(data_x[0 : train_size])
train_y = np.array(data_y[0: train_size])

test_size = len(data_y) - train_size
test_x = np.array(data_x[train_size:len(data_x)])
test_y = np.array(data_y[train_size:len(data_y)])

# 모델 생성
model = Sequential()
model.add(LSTM(units=10, activation='relu', return_sequences=True, input_shape=(window_size, data_size)))
model.add(Dropout(0.1))
model.add(LSTM(units=10, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(units=1))
model.summary()

model.compile(optimizer='adam',loss='mean_squared_error')
history = model.fit(train_x, train_y, epochs=60, batch_size=30)


pred_y = model.predict(test_x)
print(pred_y)

print("Tomorrow's SEC price: ", raw_df.close[-1], pred_y[-1],dfy.close[-1])
print("Tomorrow's SEC price: ", raw_df.close[-1] / dfy.close[-1] * pred_y[-1, 'KRW'])