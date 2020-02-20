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


from sklearn import linear_model
df_clean = df.loc[df['state'] == 1]
y = df_clean['goal_in_usd']
X = df_clean['pledged_in_usd']
lr = linear_model.LinearRegression()
model = lr.fit(X.values.reshape(-1,1) ,y)

print(model.coef_)
print(model.intercept_)