from Data import Data
import numpy as np

# Tworzymy obiekt klasy Data, który w inicie pobiera kickstarter.tsv
data_object = Data()

# By dostać się do Data_Frame musimy pobrać atrybut utworzonego obiektu
df = data_object.data

#pobieramy 5% zbioru do testów
y='state'

x_rest, x_dev, y_rest, y_dev = data_object.dev_data(y)

print(np.shape(x_dev), x_dev.describe())


