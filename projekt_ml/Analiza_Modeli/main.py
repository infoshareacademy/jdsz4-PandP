from Data import Data

# Tworzymy obiekt klasy Data, który w inicie pobiera kickstarter.tsv
data = Data()

# By dostać się do Data_Frame musimy pobrać atrybut utworzonego obiektu
df = data.data
print(df)
print(df.head())
print(df.columns)


# jeśli chcemy jako y mieć kolumne 'state' to w ten sposob:
y = df['state']
print('\n', y.describe())
# jeśli chcemy jako x mieć kolumny 'main_category' i 'goal' to w ten sposob:
x = df[['main_category','goal_in_usd' ]]
print('\n', x.describe())








