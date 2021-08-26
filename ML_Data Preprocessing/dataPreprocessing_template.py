# Data_Preprocessing Template


# Importing the libraries
import numpy as np #contains mathmetical tools
import matplotlib.pyplot as plt
import pandas as pd # to import and manage dataset


# Importing the dataset
dataset = pd.read_csv('DataPreprocessing.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values


#Taking care of missing data



"""from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer = imputer.fit(X[:, 1:3])
X[:,1:3] = imputer.transform(X[:, 1:3])"""



# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


#Feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""