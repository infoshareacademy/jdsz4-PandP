from Model import Model
import sklearn

class Decision_Tree_Classifier(Model):
    def __init__(self,parameters):
        self.parameters=parameters
        self.model=self.make_model()

    def make_model(self):
        model=sklearn.tree.DecisionTreeClassifier()
        return model

    def fit(self,x_train,y_train):
        self.model.fit(x_train,y_train)

    def predict(self,x_test):
        y_pred=self.model.predict(x_test)
        return y_pred

    def validation(self):
        pass