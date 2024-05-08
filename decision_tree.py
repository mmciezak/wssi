import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None,*,value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value
        #self.value = None

    def is_leaf_node(self): #czy Node jest leaf Nodem, powie nam jesli value istnieje to jest leaf node
        return self.value is not None

class DecisionTree:
    def __init__(self, min_samples_split=2, max_depth=100, n_features=None):
        self.min_samples_split = min_samples_split
        self.max_depth = max_depth
        self.n_features = n_features
        self.root = None


    def fit(self, x, y):
        self.n_features = x.shape[1] if not self.n_features else min(x.shape[1],self.n_features)
        self.root = self._grow_tree(x,y)

    def _grow_tree(self, x, y, depth=0):
        n_samples, n_feats = x.shape
        n_labels = len(np.unique(y))
        
        #sprawdz punkt zatrzymania
        if depth>=self.max_depth or n_labels==1 or n_samples<self.min_samples_split:
            leaf_value = self._most_common_label(y)
            return Node(value=leaf_value)
            
        feat_idx = np.random.choice(n_feats, self.n_features, replace=False)

        #znajdz najlepsze miejsce do podzialu
        best_thresh, best_feature = self._best_split(x,y,feat_idx)


        #podziel na poddrzewa
        #...

    def _best_split(self,x,y,feat_idxs):
        best_gain = -1
        split_idx, split_threshold = None, None

        #sprawdzamy wszystkie mozliwe opcje i zwracamy najlepsza
        for feat_idx in feat_idxs:
            x_column = x[:, feat_idx]
            threshold = np.unique(x_column)

            for thr in threshold:
                gain = self._information_gain(y,x_column, thr)

                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split__threshold = thr

        return split_threshold, split_idx

    def _information_gain(self, y, X_column, threshold):
        #entropia rodzica
        parent_entropy = self._entropy(y)

        return 1
        

    def _split(self, X_column, split_thresh):
        pass

    def _entropy(self, y):#x
        hist = np.bincount(y)
        ps = hist / len(y)
        return -np.sum([p*np.log(p) for p in ps if p>0])

    def _traverse_tree(self, x, node):
        pass

    def predict(self, X):#x
        return np.array([self._traverse_tree(x,self.root) for x in X])







    def _most_common_label(self, y):
        counter = Counter(y)
        value = counter.most_common(1)[0][0]
        return value
