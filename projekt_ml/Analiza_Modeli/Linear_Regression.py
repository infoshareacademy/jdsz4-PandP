from Model import Model

class Linear_Regression(Model):
    def __init__(self):
        self.model=self.make_model('hello')

    def make_model(self, parameters):
        #sklearn.linear_model.LinearRegression()
        print('Utworzono obiekt klasy Linear_Regression')
        pass
        return 0

    def fit(self,x_train,y_train):
        pass

    def predict(self,x_test):
        pass

    def validation(self):
        pass