import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_predict, cross_val_score, KFold
from sklearn.metrics import confusion_matrix
from sklearn.externals import joblib


def load_data():
    df = pd.read_csv('../data/cs-training.csv', index_col=0)
    # drop rows with missing column data
    df.dropna(inplace=True)
    
    target = 'SeriousDlqin2yrs'
    
    X = df.drop(target, axis=1)
    y = df[target]
    return X, y


X, y = load_data()
folds = KFold(5, random_state=1773)
clf = GaussianNB()


# calculate confusion matrix and accuracy
oof_preds = cross_val_predict(clf, X, y, cv=folds)
matrix = confusion_matrix(oof_preds, y)
score = cross_val_score(clf, X, y, scoring='roc_auc', cv=folds).mean()

print "\nmodel results"
print "-------------\n"
print "auc: {}".format(score.mean())
print "\n-- confusion matrix --\n"
print matrix


# train model on entire dataset
clf.fit(X, y)


# save model
joblib.dump(clf, 'credit_model/model/nb.gz', protocol=2)
