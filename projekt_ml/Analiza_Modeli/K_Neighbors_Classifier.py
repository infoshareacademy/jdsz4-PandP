from Model import Model
import sklearn
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

class K_Neighbors_Classifier(Model):
    def __init__(self,parameters):
        self.parameters=parameters
        self.model=self.make_model()

    def make_model(self):
        model=KNeighborsClassifier(self.parameters)
        return model

    def normalize_data(self,x_train, x_test):
        scaler = sklearn.preprocessing.MinMaxScaler()
        scaler.fit(x_train)
        x_train = scaler.transform(x_train)
        x_test = scaler.transform(x_test)
        return x_train, x_test

    def fit(self,x_train,y_train):
        self.model.fit(x_train,y_train)

    def predict(self,x_test):
        y_pred=self.model.predict(x_test)
        return y_pred

    def accuracy_score(self,y_test,y_pred):
        acc_score=sklearn.metrics.accuracy_score(y_test,y_pred)
        return acc_score

    def validation(self,x_train, y_train):
        val_score=cross_val_score(self.model, x_train, y_train, cv=5)
        return np.mean(val_score)