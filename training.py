from sklearn import datasets
from sklearn.model_selection import train_test_split
from decision_tree_2 import DecisionTree
import numpy as np

data = datasets.load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
)

clf = DecisionTree(max_depth=10)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

def accuracy(y_test, y_pred):
    return np.sum(y_test == y_pred) / len(y_test)

acc = accuracy(y_test, predictions)
print(acc)


#a = np.array([3,1,2,3,6,8,7,1,2,3])
#print(np.bincount(a))

#b = np.arange(5)
#print(b)
#print(np.argwhere(b<3))
#print(np.argwhere(b<3).flatten())
