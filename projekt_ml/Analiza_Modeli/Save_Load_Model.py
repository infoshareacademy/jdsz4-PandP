import pickle

class Save_Load_Model():
    def __init__(self):
        pass

    def save_model(self,model):
        filename = 'finalized_model.sav'
        pickle.dump(model, open(filename, 'wb'))

    def load_model(self, filename):
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.score(X,y)
        print(result)