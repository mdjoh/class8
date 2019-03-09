#!usr/bin/env python

from sklearn.datasets import load_iris
from sklearn.datasets import load_boston
import sklearn.datasets

[func for func in dir(sklearn.datasets) if func.startswith("load")]
# lists all functions in library that start with load

iris_data = load_iris()
dir(iris_data) #lists all the properties of iris_data
#output: ['DESCR', 'data', 'feature_names', 'filename', 'target', 'target_names']

# DESCR: type str; description explains variable characteristics, summary stats, creator, history of dataset, references
# data: type numpy array; actual data of dataset in numpy array form
# feature_names: type list; variable names
# filename: type str; the full directory of where dataset is located
# target: type numpy array; 1x rows, containing the thing we're trying to predict
# target_names: numpy array; name of the class we're predicting in the categorical case

# To do:
# visualize your data from loading it from importing it from sklearn
#	-this can actually include converting to pandas, and running your script from before
# train and apply either a KNN-classifier or KNN-regressor on your dataset
# print the output "score" or "performance" of the classifier/regressor
# if done correctly, the score will NOT be perfect
