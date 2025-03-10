import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#kanserin iyi huylu, kötü huylu olduğunu gösteren bir veri seti.
df = pd.read_csv("data.csv")
df.head()
print(df.info())
df.shape
df.T.describe()
df.drop(["Unnamed: 32", "id"],axis=1,inplace= True)
print(df.info())
df.diagnosis =[1 if each =="M" else 0 for each in df.diagnosis]
print(df.info())
y = df.diagnosis.values
x_data = df.drop(["diagnosis"],axis = 1)
#normalization işlemi 

# x = (x_data - np.min(x_data))/(np.max(x_data) - np.min(x_data)).values //bu satırda 'float' object has no attribute 'values' hatası alabılırsınız. Bunun için aşağıdaki yöntemi kullanabilirsiniz.

# Yöntem 1:
#  Minimum ve maksimum değerleri aynı olan sütunları bul
constant_columns = x_data.columns[x_data.min() == x_data.max()]
print("Sabit sütunlar:", constant_columns)

# Eğer sabit sütunlar varsa, onları düşür
x_data = x_data.drop(columns=constant_columns)

# Tekrar normalize et
x = (x_data - x_data.min()) / (x_data.max() - x_data.min())

print(x.describe())  # Normalizasyonun başarılı olup olmadığını doğrula

# Yöntem 2: 
#x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data))


df.head()
#train test split
from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test = train_test_split(x,y,test_size= 0.2, random_state= 42)
x_train = x_train.T
x_test = x_test.T
y_train = y_train.T
y_test = y_test.T
print("x_train: ",x_train.shape)
print("x_test: ",x_test.shape)
print("y_train: ",y_train.shape)
print("y_test: ",y_test.shape)
print(x.describe().T)
#parameter initialize and sigmoid function
#dimension = 30
def initialize_function(dimension):
    w = np.full((dimension,1),0.01)
    b = 0.0
    return w,b
def sigmoid_function(z):
    y_head = 1/(1+np.exp(-z))
    return y_head
sigmoid_function(0)
sigmoid_function(7)
def forward_backward_function(w,b,x_train,y_train):
    #forward
    z = np.dot (w.T,x_train)
    y_head = sigmoid_function(z)
    loss = -y_train*np.log(y_head)-(1-y_head)*np.log(1-y_head)
    cost =(np.sum(loss)/x_train.shape[1])

    #backward 
    derivative_weight = (np.dot(x_train,((y_head-y_train).T)))/x_train.shape[1]
    derivative_bias = (np.dot(x_train,((y_head-y_train).T)))/x_train.shape[1]
    gradients = {"weights: ", derivative_weight, "bias: ", derivative_bias} # tuple'da saklıyoruz.
    
    return cost, gradients
# Updating(learning) parameters
def update(w, b, x_train, y_train, learning_rate,number_of_iterarion):
    cost_list = []
    cost_list2 = []
    index = []
    # updating(learning) parameters is number_of_iterarion times
    for i in range(number_of_iterarion):
        # make forward and backward propagation and find cost and gradients
        cost,gradients = forward_backward_propagation(w,b,x_train,y_train)
        cost_list.append(cost)
        # lets update
        w = w - learning_rate * gradients["derivative_weight"]
        b = b - learning_rate * gradients["derivative_bias"]
        if i % 10 == 0:
            cost_list2.append(cost)
            index.append(i)
            print ("Cost after iteration %i: %f" %(i, cost))
    # we update(learn) parameters weights and bias
    parameters = {"weight": w,"bias": b}
    plt.plot(index,cost_list2)
    plt.xticks(index,rotation='vertical')
    plt.xlabel("Number of Iterarion")
    plt.ylabel("Cost")
    plt.show()
    return parameters, gradients, cost_list
#parameters, gradients, cost_list = update(w, b, x_train, y_train, learning_rate = 0.009,number_of_iterarion = 200)
# prediction
def predict(w,b,x_test):
    # x_test is a input for forward propagation
    z = sigmoid(np.dot(w.T,x_test)+b)
    Y_prediction = np.zeros((1,x_test.shape[1]))
    # if z is bigger than 0.5, our prediction is sign one (y_head=1),
    # if z is smaller than 0.5, our prediction is sign zero (y_head=0),
    for i in range(z.shape[1]):
        if z[0,i]<= 0.5:
            Y_prediction[0,i] = 0
        else:
            Y_prediction[0,i] = 1

    return Y_prediction
# predict(parameters["weight"],parameters["bias"],x_test)
def logistic_regression(x_train, y_train, x_test, y_test, learning_rate ,  num_iterations):
    # initialize
    dimension =  x_train.shape[0]  # that is 4096
    w,b = initialize_weights_and_bias(dimension)
    # do not change learning rate
    parameters, gradients, cost_list = update(w, b, x_train, y_train, learning_rate,num_iterations)
    
    y_prediction_test = predict(parameters["weight"],parameters["bias"],x_test)
    y_prediction_train = predict(parameters["weight"],parameters["bias"],x_train)

    # Print train/test Errors
    print("train accuracy: {} %".format(100 - np.mean(np.abs(y_prediction_train - y_train)) * 100))
    print("test accuracy: {} %".format(100 - np.mean(np.abs(y_prediction_test - y_test)) * 100))
    
logistic_regression(x_train, y_train, x_test, y_test,learning_rate = 0.01, num_iterations = 150)
#use sklearn LR
from sklearn.linear_model import LogisticRegression
lr  = LogisticRegression()
lr.fit(x_train.T,y_train.T)
print("test data accuary:  {}".format(lr.score(x_test.T,y_test.T))) #lr..score (predict and score)


