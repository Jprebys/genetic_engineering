import pandas as pd
import numpy as np

def top10_accuracy_scorer(estimator, X, y):  
    """A custom scorer that evaluates a model on whether the correct label is in 
    the top 10 most probable predictions.

    Args:
        estimator (sklearn estimator): The sklearn model that should be evaluated.
        X (numpy array): The validation data.
        y (numpy array): The ground truth labels.

    Returns:
        float: Accuracy of the model as defined by the proportion of predictions
               in which the correct label was in the top 10. Higher is better.
    """
    # predict the probabilities across all possible labels for rows in our training set
    probas = estimator.predict_proba(X)
    
    # get the indices for top 10 predictions for each row; these are the last ten in each row
    # Note: We use argpartition, which is O(n), vs argsort, which uses the quicksort algorithm 
    # by default and is O(n^2) in the worst case. We can do this because we only need the top ten
    # partitioned, not in sorted order.
    # Documentation: https://numpy.org/doc/1.18/reference/generated/numpy.argpartition.html
    
    
    top10_idx = np.argpartition(probas, -10, axis=1)[:, -10:]
    
    # index into the classes list using the top ten indices to get the class names
    top10_preds = estimator.classes_[top10_idx]

    # check if y-true is in top 10 for each set of predictions
    mask = top10_preds == y.reshape((y.size, 1))
    
    # take the mean
    top_10_accuracy = mask.any(axis=1).mean()
 
    return top_10_accuracy




def get_ngram_features(data, subsequences, overlapping=False):
    """Generate counts for each subsequence.

    Args:
        data (DataFrame): The data you want to create features from. Must include a "sequence" column.
        subsequences (list): A list of subsequences to count.
        overlapping (bool): True if you want overlapping counts, False by default

    Returns:
        DataFrame: A DataFrame with one column for each subsequence.
    """
    features = pd.DataFrame(index=data.index)
    
    for subseq in subsequences:
        if overlapping:
            features[subseq] = data.sequence.apply(find_overlapping, args=(subseq, ))
        else:
            features[subseq] = data.sequence.str.count(subseq)
        
            
    return features


def find_overlapping(seq, subseq):
    """Count overlapping occurences of a given substring in a given string"""
    
    pos, count = 0, 0
    while True:
        pos = seq.find(subseq, pos)
        if pos < 0:
            break
        pos += 1    
        count += 1
    return count   
    
    

def get_training_data():
    """Load the training data from the data folder
    and return two DataFrames"""
    
    X = pd.read_csv('../data/train_values.csv').set_index('sequence_id')
    y = pd.read_csv('../data/train_labels.csv').set_index('sequence_id')
    return X, y



def get_perms(n):
    """Return list of permutations with length n"""
    
    from itertools import permutations
    bases = 'CATGN'
    return [''.join(perm) for perm in permutations(bases, n)]
    
    