# deep learning
# activation functions:
# sigmoid function
# hyperbolic tangent
# rectified linear unit(ReLU)

import numpy

from sklearn.datasets import load_iris

iris = load_iris()
print(type(iris))

# type of iris is: sklearn.utils.Bunch
print(iris.DESCR)

X = iris.data

# X
y = iris.target

print(y)

# class 0 --> [1.0.0]
# class 1 --> [0,1,0]
# class 2 --> [0,0,1]

# transform each into a vector of 3
from keras.utils import to_categorical
y = to_categorical(y)
print(y.shape)
print(y.shape)

# split the training data and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

# note the data is shuffled for us so we're not training a bunch of 0's then suddenly hit the 1s

#standardize the data
from sklearn.preprocessing import MinMaxScaler

scaler_object = MinMaxScaler()

scaler_object.fit(X_train)

scaled_X_train = scaler_object.transform(X_train)
#note these are now all between 0 and 1
print(scaled_X_train)
scaled_X_test = scaler_object.transform(X_test)

X_train.max()
scaled_X_train.max()

print(X_train)
print(scaled_X_train)

from keras.models import Sequential
from keras.layers import Dense

#may need to tweak the hyperparameters below

model = Sequential()
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print(model.summary())

# fit and train the model
# Play around with number of epochs as well!
print(model.fit(scaled_X_train,y_train,epochs=150, verbose=2))

# print prediction of model classes (the index positions)
print(model.predict(scaled_X_test))
print(model.predict_classes(scaled_X_test))

# evaluate model performance
# compare predictions against y test

print(model.metrics_names)

print(model.evaluate(x=scaled_X_test,y=y_test))

from sklearn.metrics import confusion_matrix,classification_report

predictions = model.predict_classes(scaled_X_test)
print(f'predictions: {predictions}')

y_test.argmax(axis=1)
confusion_matrix(y_test.argmax(axis=1),predictions)
print(classification_report(y_test.argmax(axis=1),predictions))

print(accuracy_score(y_test.argmax(axis=1), predictions))

# save and load models
model.save('myfirstmodel.h5')
from keras.models import load_model
newmodel = load_model('myfirstmodel.h5')
newmodel.predict_classes(X_test)
