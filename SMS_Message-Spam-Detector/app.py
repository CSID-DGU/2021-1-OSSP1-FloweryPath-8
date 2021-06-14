from flask import Flask,render_template,url_for,request
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import urllib.request
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import SimpleRNN, Embedding, Dense
from tensorflow.keras.models import Sequential
from sklearn.model_selection import StratifiedKFold
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict' ,methods=['POST'])
def predict():
    '''df = pd.read_csv('spam.csv',encoding='latin1')

    print('총 샘플의 수 :',len(df))
    del df['Unnamed: 2']
    del df['Unnamed: 3']
    del df['Unnamed: 4']
    df['v1'] = df['v1'].replace(['ham','spam'],[0,1])
    df[:5]
    print(df[:5])

    print(df.isnull().values.any())

    print(df['v2'].nunique(), df['v1'].nunique())

    df.drop_duplicates(subset=['v2'], inplace=True) # v2 열에서 중복인 내용이 있다면 중복 제거
    print('총 샘플의 수 :',len(df))

    print(df.groupby('v1').size().reset_index(name='count'))

    X_data = df['v2']
    y_data = df['v1']
    print('메일 본문의 개수: {}'.format(len(X_data)))
    print('레이블의 개수: {}'.format(len(y_data)))

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(X_data) # 5169개의 행을 가진 X의 각 행에 토큰화를 수행
    sequences = tokenizer.texts_to_sequences(X_data) # 단어를 숫자값, 인덱스로 변환하여 저장
    print(sequences[:5])

    word_to_index = tokenizer.word_index
    print(word_to_index)

    threshold = 2
    total_cnt = len(word_to_index) # 단어의 수
    rare_cnt = 0 # 등장 빈도수가 threshold보다 작은 단어의 개수를 카운트
    total_freq = 0 # 훈련 데이터의 전체 단어 빈도수 총 합
    rare_freq = 0 # 등장 빈도수가 threshold보다 작은 단어의 등장 빈도수의 총 합

    # 단어와 빈도수의 쌍(pair)을 key와 value로 받는다.
    for key, value in tokenizer.word_counts.items():
        total_freq = total_freq + value

     # 단어의 등장 빈도수가 threshold보다 작으면
    if(value < threshold):
        rare_cnt = rare_cnt + 1
        rare_freq = rare_freq + value

    print('등장 빈도가 %s번 이하인 희귀 단어의 수: %s'%(threshold - 1, rare_cnt))
    print("단어 집합(vocabulary)에서 희귀 단어의 비율:", (rare_cnt / total_cnt)*100)
    print("전체 등장 빈도에서 희귀 단어 등장 빈도 비율:", (rare_freq / total_freq)*100)

    vocab_size = len(word_to_index) + 1
    print('단어 집합의 크기: {}'.format((vocab_size)))

    n_of_train = int(len(sequences) * 0.8)
    n_of_test = int(len(sequences) - n_of_train)
    print('훈련 데이터의 개수 :',n_of_train)
    print('테스트 데이터의 개수:',n_of_test)

    X_data = sequences
    print('메일의 최대 길이 : %d' % max(len(l) for l in X_data))
    print('메일의 평균 길이 : %f' % (sum(map(len, X_data))/len(X_data)))

    max_len = 189
    # 전체 데이터셋의 길이는 max_len으로 맞춥니다.
    data = pad_sequences(X_data, maxlen = max_len)
    print("훈련 데이터의 크기(shape): ", data.shape)

    X_test = data[n_of_train:] #X_data 데이터 중에서 뒤의 1034개의 데이터만 저장
    y_test = np.array(y_data[n_of_train:]) #y_data 데이터 중에서 뒤의 1034개의 데이터만 저장
    X_train = data[:n_of_train] #X_data 데이터 중에서 앞의 4135개의 데이터만 저장
    y_train = np.array(y_data[:n_of_train]) #y_data 데이터 중에서 앞의 4135개의 데이터만 저장

    np.random.seed(max_len)
    kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=max_len) #5회 교차 검증 테스트
    cvscores = []

    for train, test in kfold.split(X_test, y_test):

        model = Sequential()
        model.add(Embedding(vocab_size, 32)) # 임베딩 벡터의 차원은 32
        model.add(SimpleRNN(32)) # RNN 셀의 hidden_size는 32
        model.add(Dense(1, activation='sigmoid'))
        model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
        model.fit(X_train, y_train, epochs=4, batch_size=64, validation_split=0.2)

    scores = model.evaluate(X_test[test], y_test[test], verbose=0)#X_test과 y_test검증
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100)) #정확도
    cvscores.append(scores[1] * 100) #cvscores에 저장

    print("%.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores))) #kfold 인증 최중결과'''

    from tensorflow.keras.models import load_model

    model = load_model("my_model.h5") #모텔 load
    if request.method == 'POST':
        message = request.form['message']
        cv = Tokenizer()
        data = [message]
        cv.fit_on_texts(data)#각 행에 토큰화를 수행
        data = cv.texts_to_sequences(data)# 단어를 숫자값, 인덱스로 변환하여 저장
        max_len = 189
        # 전체 데이터셋의 길이는 max_len으로 맞춥니다.
        vect = pad_sequences(data, maxlen=max_len)#전체 데이터셋의 길이는 max_len으로 맞춥니다.

        word_to_index = cv.word_index
        print(word_to_index)

        vocab_size = len(word_to_index) + 1
        print('단어 집합의 크기: {}'.format(vocab_size))
        my_prediction = model.predict(vect)#모텔이용해서 판단
    return render_template('result.html', prediction=my_prediction) #판단 결과 post


if __name__ == '__main__':
    app.run(debug=True)
