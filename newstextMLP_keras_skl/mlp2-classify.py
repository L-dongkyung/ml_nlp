from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn import model_selection, metrics
import json
import numpy as np

max_words = 56681  # 입력 단어 수 : word-dic.json 파일 참고
nb_classes = 6  # 6개의 카테고리
batch_size = 64
epochs = 20

# MLP 모델 생성하기
def build_model():
    model = Sequential()
    model.add(Dense(512, input_shape=(max_words,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# 데이터 읽어 들이기
# data = json.load(open("./data-mini.json"))
data = json.load(open("./data.json"))
x = data["X"]
y = data["Y"]

# 학습하기
x_train, x_test, y_train, y_test = train_test_split(x, y)
y_train = np_utils.to_categorical(y_train, nb_classes)
print(len(x_train), len(y_train))
model = KerasClassifier(build_fn=build_model, epochs=epochs, batch_size=batch_size)
model.fit(x_train, y_train)

# 예측하기
pre = model.predict(x_test)
ac_score = metrics.accuracy_score(y_test, pre)
cl_report = metrics.classification_report(y_test, y)
print("정답률=",ac_score)
print("리포트=\n", cl_report)