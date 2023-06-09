#-------------------------------------------------------------------------
# AUTHOR: Joel Joshy
# FILENAME: svm.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #3
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: YOU HAVE TO WORK WITH THE PYTHON LIBRARIES numpy AND pandas to complete this code.

#importing some Python libraries
from sklearn import metrics, svm
import numpy as np
import pandas as pd

#defining the hyperparameter values
c = [1, 5, 10, 100]
degree = [1, 2, 3]
kernel = ["linear", "poly", "rbf"]
decision_function_shape = ["ovo", "ovr"]

df = pd.read_csv('optdigits.tra', sep=',', header=None) #reading the training data by using Pandas library

X_training = np.array(df.values)[:,:64] #getting the first 64 fields to create the feature training data and convert them to NumPy array
y_training = np.array(df.values)[:,-1] #getting the last field to create the class training data and convert them to NumPy array

df = pd.read_csv('optdigits.tes', sep=',', header=None) #reading the training data by using Pandas library

X_test = np.array(df.values)[:,:64] #getting the first 64 fields to create the feature testing data and convert them to NumPy array
y_test = np.array(df.values)[:,-1] #getting the last field to create the class testing data and convert them to NumPy array



#created 4 nested for loops that will iterate through the values of c, degree, kernel, and decision_function_shape
#--> add your Python code here

highestAccuracy = 0

store_values = []
for c_value in c:
    for degree_value in degree:
        for kernel_value in kernel:
           for decision_function_shape_value in decision_function_shape:

                #Create an SVM classifier that will test all combinations of c, degree, kernel, and decision_function_shape.
                #For instance svm.SVC(c=1, degree=1, kernel="linear", decision_function_shape = "ovo")
                #--> add your Python code here
                clf = svm.SVC(C=c_value, degree = degree_value, kernel = kernel_value, decision_function_shape = decision_function_shape_value)

                #Fit SVM to the training data
                #--> add your Python code here
                clf = clf.fit(X_training, y_training)

                #make the SVM prediction for each test sample and start computing its accuracy
                #hint: to iterate over two collections simultaneously, use zip()
                #Example. for (x_testSample, y_testSample) in zip(X_test, y_test):
                #to make a prediction do: clf.predict([x_testSample])
                #--> add your Python code here
                correct = 0

                for (x_testSample, y_testSample) in zip(X_test, y_test):
                    
                    prediction = clf.predict([x_testSample])[0]
                     
                    if prediction == y_testSample: 
                         correct += 1
                currentAccuracy = correct/len(y_test)
                #check if the calculated accuracy is higher than the previously one calculated. If so, update the highest accuracy and print it together
                #with the SVM hyperparameters. Example: "Highest SVM accuracy so far: 0.92, Parameters: a=1, degree=2, kernel= poly, decision_function_shape = 'ovo'"
                #--> add your Python code here
                if currentAccuracy > highestAccuracy:
                    highestAccuracy = currentAccuracy
                    print("Current Highest Accuracy: " + str(highestAccuracy) + "\nC = " + str(c_value) + "\nDegree = " + str(degree_value) + "\nKernel = " + kernel_value+ "\nDecison Function Shape = " + decision_function_shape_value) 
                    store_values.append([str(highestAccuracy), str(c_value), str(degree_value), kernel_value, decision_function_shape_value])
print("\nCOMPLETE!")
print("Highest Accuracy after all comparisons: " + store_values[-1][0] + "\nC = " + store_values[-1][1]  + "\nDegree = " + store_values[-1][2] + "\nKernel = " + store_values[-1][3] + "\nDecision Function Shape = " + store_values[-1][4]) 






