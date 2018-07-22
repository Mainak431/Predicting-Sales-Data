from keras.models import Sequential
from keras.layers import Dense
import numpy
import csv
import os
# fix random seed for reproducibility
numpy.random.seed(7)
# load pima indians dataset
# split into input (X) and output (Y) variables
def num(n):
    if len(n) == 1:
        return (ord(n))
    # ord returns ascii value
    else:
        l = []
        for i in n:
            l.append(ord(i))
        return (sum(l))
    # returning sum of ascii values for strings as sum


with open('train.csv', 'r', ) as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    listi = list(spamreader)
    l = listi[0]
    # extracting column informations
    # print(l)
    length = (len(l))
    # length is no of features
    arr = [[] for i in range(length)]
    leni = (len(listi))
    for i in range(1, leni):
        for j in range(length):
            if listi[i][j].isnumeric():
                arr[j].append(int(listi[i][j]))
            else:
                arr[j].append(num(listi[i][j]))
                # ord gives ascii value
    meani = []
    std = []
    for i in range(length):
        meani.append(numpy.mean(arr[i]))
        std.append(numpy.std(arr[i]))
        # mean and standard Deviation
    norm = [[] for i in range(length)]
    # normalization by mean and standard deviation
    for i in range(length):
        for j in arr[i]:
            if i != length - 1:
                norm[i].append((j - meani[i]) / std[i])
            else:
                norm[i].append(j)

    y = norm[length - 1]
    del(norm[0])
    Xi = numpy.zeros((len(norm[0]),len(norm)))
    for i in range(len(norm[0])):
        for j in range(len(norm)):
            Xi[i][j] = norm[j][i]
    X = Xi[:,0:15]
    Y = Xi[:,15]
    print(Y)

    model = Sequential()
    model.add(Dense(12, input_dim=len(norm)-1, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    model.fit(X, Y, epochs=50, batch_size=10)
    # evaluate the model
    scores = model.evaluate(X, Y)
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    with open('test.csv', 'r', ) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        listi = list(spamreader)
        l = listi[0]
        # extracting column informations
        # print(l)
        length = (len(l))
        # length is no of features
        arr = [[] for i in range(length)]
        leni = (len(listi))
        for i in range(1, leni):
            for j in range(length):
                if listi[i][j].isnumeric():
                    arr[j].append(int(listi[i][j]))
                else:
                    arr[j].append(num(listi[i][j]))

        norm = [[] for i in range(length)]
        # normalization by mean and standard deviation
        for i in range(length):
            for j in arr[i]:
                if i != length - 1:
                    norm[i].append((j - meani[i]) / std[i])
                else:
                    norm[i].append(j)
        del (norm[0])
        Xi = numpy.zeros((len(norm[0]), len(norm)))
        for i in range(len(norm[0])):
            for j in range(len(norm)):
                Xi[i][j] = norm[j][i]
        print(Xi)
        X_test = Xi
        predicted = model.predict_classes(X_test[:])
        print(predicted)
        with open('resultmakei.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            spamwriter.writerow(['id'] + ['P'])
            rows = [[] for i in range(len(predicted))]
            for i in range(len(predicted)):
                rows[i].append(arr[0][i])
                rows[i].append(predicted[i][0])
            # print(rows)
            spamwriter.writerows(rows)
