import pandas as pd


class Data():
    def __init__(self):
        self.data = self.load_csv()

    def convert_state(self,x):
        # funkcja zmienia wartości tak by kampanie z sukcesem miały wartośc 1, a z porażką 0
        if x == 'failed' or x == 'canceled':
            return 0
        elif x == 'successful':
            return 1

    def convert_main_category(self,x):
        # funkcja zmienia wartości tak by głowne kategorie były liczbami, a nie stringami
        if x == 'Fashion':
            return 0
        elif x == 'Film & Video':
            return 1
        elif x == 'Art':
            return 2
        elif x == 'Technology':
            return 3
        elif x == 'Journalism':
            return 4
        elif x == 'Publishing':
            return 5
        elif x == 'Games':
            return 6
        elif x == 'Theater':
            return 7
        elif x == 'Music':
            return 8
        elif x == 'Photography':
            return 9
        elif x == 'Design':
            return 10
        elif x == 'Food':
            return 11
        elif x == 'Crafts':
            return 12
        elif x == 'Comics':
            return 13
        elif x == 'Dance':
            return 14

    def load_csv(self):
        data = pd.read_csv('kickstarter_filtered.tsv', sep='\t')
        data = data[['name', 'main_category', 'category', 'country', 'launched',
                     'deadline', 'duration', 'currency', 'goal_in_usd', 'pledged_in_usd',
                     'percentage_of_money_collected', 'backers', 'state']]

        data['state'] = data['state'].apply(self.convert_state)
        data['main_category'] = data['main_category'].apply(self.convert_main_category)
        return data
