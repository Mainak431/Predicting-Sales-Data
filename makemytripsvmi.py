from sklearn import svm, metrics
import csv
import numpy
import os
import pickle
import matplotlib.pyplot as plt

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
    print(l)
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
    del(norm[length-1])
    del(norm[0])
    plt
    norm = numpy.transpose(norm)
    X_train = norm
    Y_train = y
    print(X_train)
    with open('test.csv', 'r', ) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        listi = list(spamreader)
        l = listi[0]
        # extracting column informations
        print(l)
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
        X_test = norm
        del(X_test[0])
        #X_test is the input test data
        param_C = 5
        param_gamma = 0.05
        #SVM starts from here
        classifier = svm.SVC(kernel='linear', C=param_C, gamma=param_gamma)
        classifier.fit(X_train, Y_train)
        X_test = numpy.transpose(X_test)
        print(X_test)
        predicted = classifier.predict(X_test)
        print(predicted)
with open('resulti.csv', 'w',newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['id'] + ['P'])
    rows = [[] for i in range(len(predicted))]
    for i in range(len(predicted)):
        rows[i].append(arr[0][i])
        rows[i].append(predicted[i])
    print(rows)
    spamwriter.writerows(rows)

