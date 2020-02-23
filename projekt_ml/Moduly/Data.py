import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

class Data():
    def __init__(self):
        self.data, self.encoders  = self.load_csv()

    def convert(self,x):
        le = preprocessing.LabelEncoder()
        le.fit(x)
        x_convert = le.transform(x)
        return x_convert, le

    def load_csv(self):
        data = pd.read_csv('kickstarter_filtered.tsv', sep='\t')
        data = data[['name', 'main_category', 'category', 'country', 'duration',
                     'currency', 'goal_in_usd', 'pledged_in_usd',
                     'percentage_of_money_collected', 'backers', 'state']]

        encoders={}
        for element in ['main_category', 'category', 'country', 'currency', 'state']:
            tmp, tmp_encoder = self.convert(data[element])
            data[element]=tmp
            encoders[element]=tmp_encoder

        return data, encoders

    def dev_data(self, y_name, test_percent=0.05, random_state=42):
        y = self.data[y_name]
        tmp=self.data
        tmp.pop(y_name)
        x = tmp
        return train_test_split(x, y, test_size=test_percent, random_state=random_state)